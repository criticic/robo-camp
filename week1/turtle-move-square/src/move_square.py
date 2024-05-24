#!/usr/bin/env python

from genpy.message import math
import rospy
from geometry_msgs.msg import Twist
import time

def move_square():
    rospy.init_node('move_square', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    move_cmd = Twist()

    linear_speed = 0.5
    angular_speed = 0.2
    side_duration = 2
    turn_duration = (math.pi / 2) / angular_speed

    while not rospy.is_shutdown():
        for _ in range(4):
            move_cmd.linear.x = linear_speed
            move_cmd.angular.z = 0
            start_time = time.time()
            while time.time() - start_time < side_duration:
                pub.publish(move_cmd)
                rate.sleep()
            
            move_cmd.linear.x = 0
            pub.publish(move_cmd)
            rospy.sleep(1)

            move_cmd.angular.z = angular_speed
            start_time = time.time()
            while time.time() - start_time < turn_duration:
                pub.publish(move_cmd)
                rate.sleep()
            
            move_cmd.angular.z = 0
            pub.publish(move_cmd)
            rospy.sleep(1)
        
        break

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass

