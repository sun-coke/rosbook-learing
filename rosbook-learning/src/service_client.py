#!/usr/bin/env python
import rospy
from basic.srv import  WordCount

import sys

rospy.init_node('service_client')
rospy.wait_for_service('word_count')
word_count = rospy.ServiceProxy('word_count',WordCount)
words = ' '.join(sys.argv[1:])
word_count = word_count(words)
print(words,'->',word_count.count)
