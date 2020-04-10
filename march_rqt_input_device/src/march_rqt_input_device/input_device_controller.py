import rospy
import std_msgs.msg

from march_shared_resources.msg import Error, GaitInstruction


class InputDeviceController(object):
    def __init__(self, ping):
        self._instruction_gait_pub = rospy.Publisher('/march/input_device/instruction', GaitInstruction, queue_size=10)
        self._error_pub = rospy.Publisher('/march/error', Error, queue_size=10)

        self._ping = ping

        if self._ping:
            self._alive_pub = rospy.Publisher('/march/input_device/alive', std_msgs.msg.Time, queue_size=10)
            period = rospy.Duration().from_sec(0.2)
            self._alive_timer = rospy.Timer(period, self._timer_callback)

    def __del__(self):
        self._instruction_gait_pub.unregister()
        self._error_pub.unregister()
        if self._ping:
            self._alive_timer.shutdown()
            self._alive_timer.join()
            self._alive_pub.unregister()

    def _timer_callback(self, event):
        self._alive_pub.publish(event.current_real)

    def publish_increment_step_size(self):
        rospy.logdebug('Mock Input Device published step size increment')
        self._instruction_gait_pub.publish(GaitInstruction(std_msgs.msg.Header(stamp=rospy.Time.now()),
                                                           GaitInstruction.INCREMENT_STEP_SIZE, ''))

    def publish_decrement_step_size(self):
        rospy.logdebug('Mock Input Device published step size decrement')
        self._instruction_gait_pub.publish(GaitInstruction(std_msgs.msg.Header(stamp=rospy.Time.now()),
                                                           GaitInstruction.DECREMENT_STEP_SIZE, ''))

    def publish_gait(self, string):
        rospy.logdebug('Mock Input Device published gait: ' + string)
        self._instruction_gait_pub.publish(GaitInstruction(std_msgs.msg.Header(stamp=rospy.Time.now()),
                                                           GaitInstruction.GAIT, string))

    def publish_stop(self):
        rospy.logdebug('Mock Input Device published stop')
        self._instruction_gait_pub.publish(GaitInstruction(std_msgs.msg.Header(stamp=rospy.Time.now()),
                                                           GaitInstruction.STOP, ''))

    def publish_continue(self):
        rospy.logdebug('Mock Input Device published continue')
        self._instruction_gait_pub.publish(GaitInstruction(std_msgs.msg.Header(stamp=rospy.Time.now()),
                                                           GaitInstruction.CONTINUE, ''))

    def publish_pause(self):
        rospy.logdebug('Mock Input Device published pause')
        self._instruction_gait_pub.publish(GaitInstruction(std_msgs.msg.Header(stamp=rospy.Time.now()),
                                                           GaitInstruction.PAUSE, ''))

    def publish_error(self):
        rospy.logdebug('Mock Input Device published error')
        self.error_pub.publish(Error(std_msgs.msg.Header(stamp=rospy.Time.now()),
                                     'Fake error thrown by the develop input device.', Error.FATAL))

    def publish_sm_to_unknown(self):
        rospy.logdebug('Mock Input Device published state machine to unknown')
        self.instruction_gait_pub.publish(GaitInstruction(std_msgs.msg.Header(stamp=rospy.Time.now()),
                                                          GaitInstruction.UNKNOWN, ''))
