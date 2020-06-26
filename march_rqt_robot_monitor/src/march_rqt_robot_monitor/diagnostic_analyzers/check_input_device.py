from diagnostic_updater import FrequencyStatusParam, HeaderlessTopicDiagnostic
import rospy

from march_shared_resources.msg import Alive


class CheckInputDevice(object):
    """Base class to diagnose whether the input devices are connected properly."""

    def __init__(self, updater):
        self._tolerance = 0.1
        self._window_size = 10
        self._min_frequency = 5
        self._max_frequency = 5

        self._goal_sub = rospy.Subscriber('/march/input_device/alive', Alive, self._cb)

        self._frequency_params = FrequencyStatusParam({'min': self._min_frequency, 'max': self._max_frequency},
                                                      self._tolerance, self._window_size)
        self._updater = updater
        self._diagnostics = {}

    def _cb(self, msg):
        """
        Update the frequency diagnostics for given input device.

        :type msg: march_shared_resources.msg.Alive
        :param msg: Alive message
        """
        if msg.id in self._diagnostics:
            self._diagnostics[msg.id].tick()
        else:
            self._diagnostics[msg.id] = HeaderlessTopicDiagnostic('input_device {0}'.format(msg.id),
                                                                  self._updater, self._frequency_params)
            self._updater.force_update()
