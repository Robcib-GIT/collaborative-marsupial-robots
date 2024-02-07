#!/usr/bin/env python
#! /usr/bin/env python

from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
import rospy
import numpy as np
import time
global c
c=0

def callback_pointcloud(data):
    global c
    assert isinstance(data, PointCloud2)
    gen = point_cloud2.read_points(data, field_names=("x", "y", "z"), skip_nans=True)
    
    #print("hola",len(list(gen)))
    a = []
    c=c+1
    a.append(len(list(gen)))
    if c ==10:
      print(max(a))
      c=0
    


#      #print (p[0],p[1],p[2])
#      a.append(p[0])
#    print(len(a))

def main():
    rospy.init_node('pcl_listener', anonymous=True)
    rospy.Subscriber('/os1_node/points', PointCloud2, callback_pointcloud)
    rospy.spin()

if __name__ == "__main__":
    main()

