ARG ROS_DISTRO
FROM ros:${ROS_DISTRO}-ros-base

# build catkin workspace setup
SHELL ["/bin/bash", "-c"]
ARG ROS_NODES_BASE=/opt/ros-nodes
WORKDIR ${ROS_NODES_BASE}

# ROS-Package: ROSBridge Server
EXPOSE 9090
