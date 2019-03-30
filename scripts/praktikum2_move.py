#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

velocity_publisher = rospy.Publisher(
    '/robotont/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def closing():
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)

def go(duration,x,y,z):
    for i in range(0,duration):
        vel_msg.linear.x = x
        vel_msg.linear.y = y
        vel_msg.angular.z = z
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def left(duration,x,y,z):
    for i in range(0,duration):
        vel_msg.linear.x =x
        vel_msg.linear.y=y
        vel_msg.angular.z=z
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def shape(duration,x,y,z):
    for i in range(0,duration):
        vel_msg.linear.x =x
        vel_msg.linear.y=y
        vel_msg.angular.z=z
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)


x_go=float(input('cordinate x'))
y_go=float(input('cordinate y'))
z_go=float(input('cordinate z'))
duration_go=int(input('duration go'))
x_left=float(input('cordinate x'))
y_left=float(input('cordinate y'))
z_left=float(input('cordinate z'))
duration_left=int(input('duration left'))
x_shape=float(input('cordinate x'))
y_shape=float(input('cordinate y'))
z_shape=float(input('cordinate z'))
duration_shape=int(input('duration shape'))
def move():
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        ########################
        # YOUR CODE HERE START #
        ########################
        go(duration_go,x_go,y_go,z_go)
        left(duration_left,x_left,y_left,z_left)
        shape(duration_shape,x_shape,y_shape,z_shape)
        ######################
        # YOUR CODE HERE END #
        ######################


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
