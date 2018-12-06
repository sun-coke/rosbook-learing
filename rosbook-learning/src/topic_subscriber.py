#!/usr/bin/env python
import rospy
from std_msgs.msg import Int64

def callback(msg):
    print(msg.data)

rospy.init_node('topic_subscriber')

sub = rospy.Publisher('counter',Int64,callback)

rospy.spin()
