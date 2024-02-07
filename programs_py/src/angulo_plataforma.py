#!/usr/bin/env python
# determina la localizacion mediante L-PC y G-PC
import open3d as o3d
import numpy as np
import copy
import rospy, time, math
import struct
import pypcd
from std_msgs.msg import Float64

from sensor_msgs import point_cloud2
from sensor_msgs.msg import PointCloud2, PointField
from std_msgs.msg import Header
import sensor_msgs.point_cloud2 as pc2

nube_local_recibida = PointCloud2()
instante_inicial = time.time()
ok = True

def callback_L_PC(data):
    global nube_local_recibida
    nube_local_recibida = data


if __name__ == "__main__":
    #global nube_local_recibida

# DEFINICON DE NODOS DE ROS PARA SUBSCRIBIR Y PUBLICAR

    rospy.init_node("pose_z")
    sub_LPCL = rospy.Subscriber("/camera/depth/points", PointCloud2, callback_L_PC)
    rate = rospy.Rate(10)
    msg = Float64()



    while not rospy.is_shutdown():
        instante_actual = time.time()
        tiempo = instante_actual - instante_inicial

# recibimiento de la nube local leida en tiempo real 
        pc = pc2.read_points(nube_local_recibida, skip_nans=True, field_names=("x", "y", "z"))
        pc_x = []
        pc_y = []
        pc_z = []
        for p in pc:
           #pc_list.append( [p[0],p[1],p[2]] )
            pc_x.append(p[0])
            pc_y.append(p[1])
            pc_z.append(p[2])
        pcd_g = [[pc_x[c], pc_y[c], pc_z[c]]for c in range(len(pc_x))]

        pcd_tem = o3d.geometry.PointCloud()
        pcd_tem.points = o3d.utility.Vector3dVector(pcd_g)
        if tiempo > 5:
            o3d.visualization.draw_geometries([pcd_tem])
            if ok:
                o3d.io.write_point_cloud("nubes_Tasar_4.pcd", pcd_tem, write_ascii=True)
                ok = False
	    
        rate.sleep()


