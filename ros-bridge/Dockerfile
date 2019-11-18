ARG ROS_DISTRO
FROM ros:${ROS_DISTRO}-ros-base

RUN apt-get update \
  && apt-get install -y \
    build-essential \
    ros-${ROS_DISTRO}-rosbridge-server \
  && rm -rf /var/lib/apt/lists/*

ARG CATKIN_WS=/opt/catkin_ws
COPY catkin_ws/ ${CATKIN_WS}

# build catkin workspace setup
SHELL ["/bin/bash", "-c"]
WORKDIR ${CATKIN_WS}
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && catkin_make

# ROS-Package: ROSBridge Server
EXPOSE 9090
