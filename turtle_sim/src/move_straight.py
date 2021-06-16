#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 05:46:05 2021

@author: palash
"""
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

def pose_callback(pose):
    rospy.loginfo("Rbot x: %f, y: %f, z: %f",pose.x,pose.y,pose.theta)
    

def move(lin_vel, ang_vel):
    rospy.init_node('move_turtle', anonymous=False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    rate= rospy.Rate(10)
    vel = Twist()
    
    while not rospy.is_shutdown():
        vel.linear.x = lin_vel
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = ang_vel
        
        rospy.loginfo("lin_vel= %f:, ang_vel= %f", lin_vel, ang_vel )
        pub.publish(vel)
        rate.sleep()
        
if __name__ == '__main__':
    try:
        
#Providing linear and angular velocity through command line
        move(float(sys.argv[1]),float(sys.argv[2]))
    except rospy.ROSInterruptException:
        pass
