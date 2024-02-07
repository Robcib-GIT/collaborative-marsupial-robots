#!/usr/bin/env python
from libreria_IK import cinematica_inversa_cpr5dof
#from libreria_MV import movimiento
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
group.set_goal_position_tolerance(0.05)
group.set_goal_orientation_tolerance(0.05)
#group.set_planning_time(10.0)
#collision_object = moveit_msgs.msg.CollisionObject()
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

# DEFINICION DE LA FUNCION PARA EL MOVIMIENTO DEL PLANIFICADOR
# DEFINICION DE LA FUNCION PARA EL MOVIMIENTO DEL PLANIFICADOR
joint_goal = group.get_current_joint_values()

def MV_eval(Q):

    joint_goal = [Q[0],Q[1],Q[2],Q[3],Q[4]]
    plan1 = group.plan()
    group.go(joint_goal, wait=True)
    print " --- "
    print "Ejecucion MV correcta !!!"
    #rospy.sleep(1)

# DEFINICION DE TARGET POINTS PARA EL PLANIFICADOR
# DEFINICION DE TARGET POINTS PARA EL PLANIFICADOR
print "1------------"
Q = cinematica_inversa_cpr5dof.eval(680,0,228,0,0)
MV_eval(Q)

print "2------------"

Q = cinematica_inversa_cpr5dof.eval(1.0, -200.0, 480.0, 10.0,0.0)
MV_eval(Q)

Q = cinematica_inversa_cpr5dof.eval(1.0, 200.0, 480.0, 20.0,0.0)
MV_eval(Q)


"""print "2------------"
Q = cinematica_inversa_cpr5dof.eval(-200.0, -200.0, 528.0, 20.0,0.0)
MV_eval(Q)
print "3------------"
Q = cinematica_inversa_cpr5dof.eval(-200.0, -200.0, 528.0, 20.0,45.0)
MV_eval(Q)
print "4------------"
Q = cinematica_inversa_cpr5dof.eval(-100.0, -200.0, 528.0, 20.0,0.0)
MV_eval(Q)
print "5------------"
Q = cinematica_inversa_cpr5dof.eval(-100.0, -200.0, 528.0, -20.0,0.0)
MV_eval(Q)
print "6------------"
Q = cinematica_inversa_cpr5dof.eval(200.0, -200.0, 528.0, 20.0,0.0)
MV_eval(Q)
print "7------------"
Q = cinematica_inversa_cpr5dof.eval(300.0, -300.0, 528.0, 20.0,0.0)
MV_eval(Q)
print "8------------"
Q = cinematica_inversa_cpr5dof.eval(300.0, -300.0, 528.0, 20.0,0.0)
MV_eval(Q)"""
print "9------------"
Q = cinematica_inversa_cpr5dof.eval(680,0,228,0,0)
MV_eval(Q)

print "----"
group.stop()
moveit_commander.roscpp_shutdown()
    #pass
