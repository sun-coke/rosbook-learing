#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def scan_back(msg):
    global g_range_ahead
    g_range_ahead = min(msg.ranges)

g_range_ahead = 1

rospy.init_node('wander2')
scan_sub = rospy.Subscriber('scan',LaserScan,scan_back)
cmd_vel_pub = rospy.Publisher('cmd_vel',Twist,queue_size=1)
state_change_time = rospy.Time.now()
driving_forward = True
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    if driving_forward:
        if(g_range_ahead<0.8 or state_change_time<rospy.Time.now()):
            driving_forward = False
            state_change_time = rospy.Time.now()+rospy.Duration(3)

    else:
        if(state_change_time<rospy.Time.now()):
            driving_forward = True
            state_change_time = rospy.Time.now()+rospy.Duration(30)

    twist = Twist()

    if driving_forward:
        twist.linear.x = 0.3
    else:
        twist.angular.z = 1

    cmd_vel_pub.publish(twist)
    rate.sleep()


