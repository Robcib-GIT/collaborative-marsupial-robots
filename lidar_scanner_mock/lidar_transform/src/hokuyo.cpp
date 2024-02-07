
#include <pcl/segmentation/extract_labeled_clusters.h>
#include <ros/ros.h>
#include "std_msgs/Float32.h"
#include "sensor_msgs/LaserScan.h"
#include <ros/time.h>

ros::Publisher scan_pub;
ros::Subscriber scan_sub;

float g_SetAngle = 0;
int g_seq = 0;

void scanCallBack(const sensor_msgs::LaserScan::ConstPtr& scan2)
{
  //ROS_INFO("Cbk_hokuyo");
	int ranges = scan2->ranges.size();
	//populate the LaserScan message
	sensor_msgs::LaserScan scan;
    	//scan.header.stamp = scan2->header.stamp;
      scan.header.stamp = ros::Time::now();
    	//scan.header.frame_id = scan2->header.frame_id;
      scan.header.frame_id = "Lidar";
      scan.header.seq = g_seq++;

    	scan.angle_min = scan2->angle_min;
      //scan.angle_min = -M_PI;
    	scan.angle_max = scan2->angle_max;
      //scan.angle_max = M_PI;
    	scan.angle_increment = scan2->angle_increment;
      //scan.angle_increment = (M_PI / 180);
    	scan.time_increment = scan2->time_increment;
	scan.range_min = 0.0;

	scan.range_max = 150.0;

	scan.ranges.resize(ranges);
//	scan.intensities.resize(ranges);
	//for(int i = 0; i < ranges; i++)
  for(int i = 0; i < ranges; i++)
	{
    		//scan.ranges[i] = scan2->ranges[i] + 1;
        scan.ranges[i] = scan2->ranges[i];
				/* Falso color
				if (scan.ranges[i]<1)
				{
					scan.intensities.push_back(200);
				}
				if (scan.ranges[i]>1)
				{
					scan.intensities.push_back(200);
				} */
				scan.intensities.push_back(i);

	}
	scan_pub.publish(scan);
	// ROS_INFO("CBack_fin_______________");

}



int main(int argc, char** argv)
{
// ROS_INFO("Inicio");
   ros::init(argc, argv, "lidar_mock_1");
   ros::NodeHandle n;

   scan_pub = n.advertise<sensor_msgs::LaserScan>("scan2",1000);
 	//scan_sub = n.subscribe<sensor_msgs::LaserScan>("/scan",1000, &Scan2::scanCallBack, this);
   scan_sub = n.subscribe<sensor_msgs::LaserScan>("scan",1000, &scanCallBack);

	   float angle = 0;

	   ros::Rate loop_rate(10);
	   while (ros::ok())
	   {
	     ROS_INFO("while_hokuyo");
	     ros::spinOnce();
	     loop_rate.sleep();
	   }
}


/*
#include <ros/ros.h>
#include "std_msgs/String.h"
#include <sensor_msgs/LaserScan.h>
#include <stdio.h>
#include <ros/time.h>

using namespace std;
float g_SetAngle = 0;
int g_seq = 0;


class Scan2{
public:
  Scan2();
private:
		ros::NodeHandle n;
    ros::Publisher scan_pub;
    ros::Subscriber scan_sub;
  void scanCallBack(const sensor_msgs::LaserScan::ConstPtr& scan2);
};

Scan2::Scan2()
{
	scan_pub = n.advertise<sensor_msgs::LaserScan>("/scan2",1000);
	//scan_sub = n.subscribe<sensor_msgs::LaserScan>("/scan",1000, &Scan2::scanCallBack, this);
  scan_sub = n.subscribe<sensor_msgs::LaserScan>("/scan",1000, &Scan2::scanCallBack, this);
}

void Scan2::scanCallBack(const sensor_msgs::LaserScan::ConstPtr& scan2)
{
   ROS_INFO("CBack");
	int ranges = scan2->ranges.size();
	//populate the LaserScan message
	sensor_msgs::LaserScan scan;
    	//scan.header.stamp = scan2->header.stamp;
      scan.header.stamp = ros::Time::now();
    	//scan.header.frame_id = scan2->header.frame_id;
      scan.header.frame_id = "Lidar";
      scan.header.seq = g_seq++;
    	//scan.angle_min = scan2->angle_min;
      scan.angle_min = -M_PI;
    	//scan.angle_max = scan2->angle_max;
      scan.angle_max = M_PI;
    	//scan.angle_increment = scan2->angle_increment;
      scan.angle_increment = (M_PI / 180);
    	scan.time_increment = scan2->time_increment;
	//scan.range_min = 0.0;
  scan.range_min = 0.1;
	//scan.range_max = 100.0;
  scan.range_max = 6.0;
	scan.ranges.resize(ranges);
	//for(int i = 0; i < ranges; i++)
  for(int i = 0; i < 360; i++)
	{
    		scan.ranges[i] = scan2->ranges[i] + 1;
	}
	scan_pub.publish(scan);
}



int main(int argc, char** argv)
{
 ROS_INFO("Inicio");
	ros::init(argc, argv, "lidar_mock_1");


	while (ros::ok())
	{
			ROS_INFO("while_hokuyo");
		Scan2 scan2;
		ros::Rate loop_rate(5);
		ros::spinOnce();
  	loop_rate.sleep();
	}

}

*/
