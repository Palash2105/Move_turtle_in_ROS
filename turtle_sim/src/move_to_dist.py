#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:17:08 2021

@author: palash
"""

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys
import time
robot_x=0

def pose_callback(pose):
    global robot_x
    rospy.loginfo('Robot X = %f\n',pose.x)
    robot_x = pose.x
    
def move(lin_vel, ang_vel, dist):
    global robot_x
    rospy.init_node('turtle_move', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rospy.Rate(10)
    
    vel = Twist()
    while not rospy.is_shutdown():
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        
        vel.angular.x = ang_vel
        vel.angular.y = 0
        vel.angular.z = 0
        
        if(robot_x >= dist):
            rospy.loginfo("robot reached destination")
            break
        pub.publish(vel)
        
        
if __name__=='__main__':
    try:
        move(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
    except rospy.ROSInterruptException:
        pass
    