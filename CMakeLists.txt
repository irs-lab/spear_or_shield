cmake_minimum_required(VERSION 2.8.3)
project(spear_or_shield)

find_package(catkin REQUIRED COMPONENTS
	  roscpp
	  rospy
	  std_msgs
	  message_generation
)

add_message_files(
   FILES
   key_msg.msg
   mouse_msg.msg
   input_msg.msg
)


 generate_messages(
  	DEPENDENCIES
  	std_msgs
 )



link_directories(
	
)

catkin_package(
  INCLUDE_DIRS include 
  CATKIN_DEPENDS roscpp rospy std_msgs
)

include_directories(
	include
 	${catkin_INCLUDE_DIRS}
)

