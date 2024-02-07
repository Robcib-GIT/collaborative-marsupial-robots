#!/usr/bin/env python
#from libreria_IK import cinematica_inversa_cpr5dof
#from libreria_MV import movimiento
#http://www.open3d.org/docs/release/tutorial/Advanced/interactive_visualization.html
# POTENCIAL VIDEOS
#http://www.open3d.org/index.php/author/administratorivcl-org/
# CODIGO
#http://www.open3d.org/docs/release/tutorial/Basic/file_io.html#mesh
import os, sys, rospy
import math
import numpy as np
import open3d as o3d
import copy
import pymesh
#from open3d import read_point_cloud
from open3d import *
from sklearn.cluster import KMeans

import pandas as pd
import matplotlib.pyplot as plt
import copy
#%matplotlib inline


""" Para leer y escribir una nueva nube de puntos """
#pcd = read_point_cloud("papel.ply") # Read the point cloud
pcd = o3d.io.read_point_cloud("nube_real_3.pcd")
o3d.visualization.draw_geometries([pcd])
#o3d.visualization.draw_geometries([pcd])

"""  """
#mesh = read_point_cloud("papel.ply") # Read the point cloud
#mesh = o3d.io.read_triangle_mesh("papel.ply")
#print(np.asarray(mesh.vertices))
#print(np.asarray(mesh.triangles))
#o3d.io.write_triangle_mesh("papel_triangle.ply", mesh, write_ascii=True)

""" Para volver cero los puntos de z y oobtener una proyeccion 2D """
#pcd = o3d.io.read_point_cloud("plantas_3.pcd")
#print(np.asarray(pcd.points)[:,:]) # imprimir los puntos
#print(np.asarray(pcd.points)[:,1]) # imprimir los puntos
#o3d.visualization.draw_geometries([pcd])

#print("Downsample the point cloud with a voxel of 0.05")
#downpcd = o3d.geometry.voxel_down_sample(pcd, voxel_size=0.05)
"""xx=np.asarray(pcd.points)[:,0]
yy=np.asarray(pcd.points)[:,1]
zz=np.asarray(pcd.points)[:,2]

pcd_g=[]
pcd_g=[[xx[j], yy[j], zz[j], zz[j]]for j in range(len(xx))]
#o3d.visualization.draw_geometries([pcd_g])

# creo una nueva nube para almacenar los datos
#pcd_1 = o3d.geometry.PointCloud()
#pcd_1.points = o3d.utility.Vector3dVector(pcd_g)


pcl_data = pcl.PointCloud_PointXYZRGB()
pcl_data.from_list(pointspcd_g_list)
# se graba la nueva nube
#o3d.io.write_point_cloud("cloud_n.pcd", pcd_1, write_ascii=True)
# se muestra la nube creada
o3d.visualization.draw_geometries([pcl_data])

"""

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(np.array([[1, 2, 3], [4, 5, 6], [14, 15, 16], [24, 25, 26]]))

# 0.2, 0.3 are the intensity of the two points
pcd.colors = o3d.utility.Vector3dVector(np.array([[1, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]])) 

o3d.visualization.draw_geometries([pcd])



