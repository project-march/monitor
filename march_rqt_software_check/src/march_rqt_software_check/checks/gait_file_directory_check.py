import rospkg
import rospy

from march_rqt_software_check.color import Color

from .launch_check import LaunchCheck


class GaitFileDirectoryCheck(LaunchCheck):

    def __init__(self):
        LaunchCheck.__init__(self, 'GaitFileDirectory', 'Gaits are loaded from the following directory',
                             'march_gait_selection', 'march_gait_selection.launch', manual_confirmation=True)

    def perform(self):
        self.launch()

        rospy.sleep(rospy.Duration.from_sec(5))
        self.stop_launch_process()
        package_name = self.get_key_from_parameter_server('/march/gait_file_package')
        file_directory = self.get_key_from_parameter_server('/march/gait_file_directory')

        try:
            rospkg.RosPack().get_path(package_name)
        except rospkg.common.ResourceNotFound:
            self.log('Package ' + str(package_name) + ' not found on local machine.', Color.Error)
            self.fail_check()

        self.log('Package name: ' + str(package_name), Color.Info)
        self.log('Gait file directory: ' + str(file_directory), Color.Info)

        self.passed = package_name is not None and file_directory is not None
        self.done = True
