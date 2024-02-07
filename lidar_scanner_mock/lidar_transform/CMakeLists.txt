cmake_minimum_required(VERSION 2.8.3)
project(lidar_transform)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
pcl_conversions
  pcl_msgs
  pcl_ros
)

#generate_messages(DEPENDENCIES std_msgs)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES lidar_transform
#  CATKIN_DEPENDS roscpp std_msgs
#  DEPENDS system_lib
)

find_package(PCL REQUIRED)
include_directories(include ${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(lidar_transform_node src/lidar_transform.cpp)
target_link_libraries(lidar_transform_node ${catkin_LIBRARIES})

add_executable(servo_mock src/servo_mock.cpp)
target_link_libraries(servo_mock ${catkin_LIBRARIES})

add_executable(lidar_mock src/lidar_mock.cpp)
target_link_libraries(lidar_mock ${catkin_LIBRARIES})

add_executable(hokuyo src/hokuyo.cpp)
target_link_libraries(hokuyo ${catkin_LIBRARIES})

#add_executable(hokuyo2PCL src/hokuyo2PCL.cpp)
#target_link_libraries(hokuyo2PCL ${catkin_LIBRARIES})
