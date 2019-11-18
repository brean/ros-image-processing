#!/bin/bash
source "/opt/ros/$ROS_DISTRO/setup.bash"
catkin_make
source "./devel/setup.bash"
roslaunch pose_estimation start.launch
