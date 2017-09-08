cmake_minimum_required(VERSION 2.8.3)
project(ros_gtts)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  message_generation
)

add_service_files(
  FILES
  TextToSpeech.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

generate_dynamic_reconfigure_options(
  cfg/GTTS.cfg
)

catkin_package(
  CATKIN_DEPENDS dynamic_reconfigure message_runtime
)

#############
## Install ##
#############

install(PROGRAMS bin/text2wave
  DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
)
install(DIRECTORY launch scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)
