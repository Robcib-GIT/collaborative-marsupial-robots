#!/usr/bin/env python
import os, sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
from geometry_msgs.msg import PoseStamped
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list

print "Ejecucion planificador !!!"
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "G1"
group = moveit_commander.MoveGroupCommander(group_name)
# Get the name of the end-effector link
end_effector_link = group.get_end_effector_link()
# Set the reference frame for pose targets
#reference_frame = "/base_link"
reference_frame = "/link_base"
# Set the arm reference frame accordingly
group.set_pose_reference_frame(reference_frame)
# Allow replanning to increase the odds of a solution
group.allow_replanning(True)
# Allow some leeway in position (meters) and orientation (radians)
group.set_goal_position_tolerance(0.01)
group.set_goal_orientation_tolerance(0.05)
#collision_object = moveit_msgs.msg.CollisionObject()
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

def eval(Q):
    Q = cinematica_inversa_cpr5dof.eval(600,100,398,0,0)
    joint_goal = group.get_current_joint_values()
    joint_goal = [Q[0],Q[1],Q[2],Q[3],Q[4]]
    group.go(joint_goal, wait=True)
    group.stop()
    moveit_commander.roscpp_shutdown()
    print " --- "
    print "Ejecucion MV correcta !!!"
    rospy.sleep(1)
    group.clear_pose_targets()
