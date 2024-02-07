# Omega
Updated for Day - 3.

Overview of folders:

A: ROS
1) uvd_description; 
    a)This involves all the mesh files (.stl format) which are used by us within this three day event.
    b)Further the urdf and rviz files created for the robot which were used in the ros simulation are stored here.
      (uvd_new.urdf is the final urdf which will be used for the day-3 presentation)
2) uvd_gazebo;
    a)This involves the launch files and the world files for ros simulation. The launch files involes our path planning algorithm, localization and move_base to initiate gazebo.
    b)In the worlds folder, there are world files (virtual environment) which were created by us using SolidWorks, Blender, Gazebo.
3)uvd_navigation;
    a)In this folder, the config folder includes the global/local costmap param files and also the local planner file to have realtime mapping.
    b)In the maps folder, there are several environment maps (.yaml format) which later are required in Rviz.
   
B: Matlab
1) UVGI_Irradiance_Calculation is the matlab file which is created to simulate the irradiance part of the project.
2) UVLamp.slx (simulink file) has the uv circuit and scopes at the end showing results which were presented during the presentation.

C: OpenCV - {detection.py & video_det.py}
1) The human detection part using computer vision was tested and slected as better method for human perception for robot rather PIR sensor.

RESULTS:
After running codes and simulation, few videos taken for presentation are uploaded on youtube.
Youtube Playlist: https://www.youtube.com/playlist?list=PLhgI9FA__F1YdLFQ6t61QBYyg65VekeYF
