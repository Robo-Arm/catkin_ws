#!/usr/bin/env python
from geometry_msgs.msg import Pose
import rosbag
import numpy as np #you need numpy

#THIS SCRIPT PROCESSES THE RAW ROSBAG FILE TO BE USED TO GENERATE TRAJECTORIES

print("Enter the file number: ") 
demo_num = input() #input the file number

filename = 'raw_demo' + str(demo_num) + '.bag'

bag = rosbag.Bag(filename) #import the bag file

initial_pose = Pose() #initiate empty pose messages
final_pose = Pose()

i = 1
first = 1
last = bag.get_message_count()
initial_time = 0

for topic, msg, t in bag.read_messages(topics='/ee_pose'): #find the initial and final pose
    if i==1:
        initial_pose = msg
    elif i==bag.get_message_count():
        final_pose = msg
    i += 1
i = 1

for topic, msg, t in bag.read_messages(topics='/ee_pose'): #find the beginning and end msg numbers
    if msg == initial_pose:
        first = i
        initial_time = t
    if msg != final_pose:
        last = i
    i += 1
i=1
last += 1

bag.close() #close the bag file

num_msgs = last-first #determine number of unique messages in bag file

with rosbag.Bag('/home/nq/iiwa_bag/demo' + str(demo_num) + '.bag', 'w') as outbag: #export trimmed bag file
    for topic, msg, t in rosbag.Bag(filename).read_messages():
        if i >= first and i <= last:
            t -= initial_time
            outbag.write(topic, msg, t)
        i+=1

bag = rosbag.Bag('/home/nq/iiwa_bag/demo' + str(demo_num) + '.bag') #import trimmed bag fiile

x = list()
y = list()
z = list() #should be t

i=0
for topic, msg, t in bag.read_messages(topics='/ee_pose'): #take the xyz (z is time here) from new bag file and add to list
    x.append(msg.position.x)
    y.append(msg.position.y)
    z.append(i)
    print(t.to_sec())
    print(msg)
    i += 1

duration = z[len(z)-1] #linear interpolation to create 100 points, with time being 10 seconds as required for the TPGMM
new_t = np.linspace(0,duration,num = 100)
new_x = np.interp(new_t, z, x)
new_y = np.interp(new_t, z, y)
z = np.linspace(0,10,num=100)

data = np.row_stack((z, new_x, new_y)) #add the lists together to create a numpy array
data = np.transpose(data) #tranpose the data so it conforms to TPGMM format
np.save('/home/nq/iiwa_bag/demo' + str(demo_num) + '.npy', data) #exports data as a .npy file

print(first,last) #prints out the first and last numbers as a sanity check
bag.close()

