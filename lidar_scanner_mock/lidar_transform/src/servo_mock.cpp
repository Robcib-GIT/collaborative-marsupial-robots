
#include <ros/ros.h>
#include "std_msgs/Float32.h"
#include <ros/time.h>

ros::Publisher g_trueAngle_pub;

float g_SetAngle = 0;

void sendAngle(float angle)
{
  std_msgs::Float32 AngMsg;
  AngMsg.data = angle;
  g_trueAngle_pub.publish(AngMsg);
}

void angleCallback(const std_msgs::Float32::ConstPtr& msg)
{
  //ROS_INFO("CBK_servo");
  const float noise = (M_PI / 360);  // 0.5deg
  float random = ((float)rand()) / (float)RAND_MAX;
  g_SetAngle = msg->data + ((random * noise) - (noise / 2));
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "servo_mock");
  ros::NodeHandle n;

  ros::Subscriber angleSubscriber = n.subscribe("setAngle", 1000, angleCallback);
  g_trueAngle_pub = n.advertise<std_msgs::Float32>("trueAngle", 1000);

  float trueAngle = 0;

  ros::Rate loop_rate(10);
  while (ros::ok())
  {
  //  ROS_INFO("while_servo");
    float angleError = g_SetAngle - trueAngle;

// Error mínimo para que se cumpla la condición
    const float changeRate = 0.1;

// Se analiza si el error es positivo o negativo
// y se setea el sigo del incremento
    if (angleError > changeRate)
    {
      angleError = changeRate;
    }

    if (angleError < -changeRate)
    {
      angleError = -changeRate;
    }

    trueAngle += angleError;

    sendAngle(trueAngle);

    //ros::spinOnce();
    ros::spinOnce();
    loop_rate.sleep();
  }
}
