#!/usr/bin/env python

import rospy
import sys
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
from moveit_msgs.msg import RobotState
from moveit_msgs.srv import GetPositionFKRequest, GetPositionFK

#THIS SCRIPT IS TO CREATE THE /EE_POSE NODE

def callback(data):
    state.joint_state=data
    test = GetPositionFKRequest()
    test.header.frame_id = "world"
    test.fk_link_names.append("tool_link_ee")
    test.robot_state = state

    rospy.wait_for_service("compute_fk")
    fk_service = rospy.ServiceProxy("compute_fk", GetPositionFK)
    resp = fk_service(test)
    pub.publish(resp.pose_stamped[0].pose)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('joint_to_pose', anonymous=True)

    rospy.Subscriber("/joint_states", JointState, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

pub = rospy.Publisher('/ee_pose', Pose, queue_size=20)

moveit_commander.roscpp_initialize(sys.argv)
robot = moveit_commander.RobotCommander()
state = robot.get_current_state()

if __name__ == '__main__':
    listener()