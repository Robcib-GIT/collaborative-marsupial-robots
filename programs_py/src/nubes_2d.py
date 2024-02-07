#!/usr/bin/env python


import math
import numpy as np
import open3d as o3d
#from open3d import read_point_cloud


def display_inlier_outlier(cloud, ind):
    inlier_cloud = cloud.select_by_index(ind)
    outlier_cloud = cloud.select_by_index(ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    #outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud],
                                      zoom=0.3412,
                                      front=[0.4257, -0.2125, -0.8795],
                                      lookat=[2.6172, 2.0475, 1.532],
                                      up=[-0.0694, -0.9768, 0.2024])



pcd = o3d.io.read_point_cloud("2.pcd")

#o3d.visualization.draw_geometries([pcd])
downpcd = pcd.voxel_down_sample(voxel_size=0.05)
#o3d.visualization.draw_geometries([downpcd])

cl, ind = downpcd.remove_radius_outlier(nb_points=16, radius=0.05)
display_inlier_outlier(downpcd, ind)

downpcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
o3d.visualization.draw_geometries([downpcd])

print("Let's draw some primitives")

# PARA ESCRIBIR UNA NUEVA NUBE DE PUNTOS
#write_point_cloud("pointcloud2.pcd", pcd)
