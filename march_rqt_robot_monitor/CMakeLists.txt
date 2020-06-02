cmake_minimum_required(VERSION 3.0.2)
project(march_rqt_robot_monitor)

find_package(catkin REQUIRED COMPONENTS
    march_shared_resources
    std_msgs
)

catkin_package(CATKIN_DEPENDS
    march_shared_resources
    std_msgs
)

catkin_python_setup()

install(DIRECTORY config launch
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

catkin_install_python(PROGRAMS scripts/${PROJECT_NAME}_node
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
