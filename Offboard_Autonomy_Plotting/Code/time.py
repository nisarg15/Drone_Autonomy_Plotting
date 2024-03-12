# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:04:14 2023

@author: Enigma
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


path = pd.read_csv('C:/Users/nisar/Downloads/path_2 .csv')

print(path)


x_pose = path["x_pose"]
y_pose = path["c"]

x1_pose = path["y_pose"]
y1_pose = path["c"]

x2_pose = path["z_pose"]
y2_pose = path["c"]





x_pose = np.array(x_pose)
y_pose = np.array(y_pose)
x1_pose = np.array(x1_pose)
y1_pose = np.array(y1_pose)
x2_pose = np.array(x2_pose)
y2_pose = np.array(y2_pose)



plt.plot(y_pose,x_pose,color = 'g',label = "right_left")
plt.plot(y1_pose,x1_pose,color = 'r',label = "back and front")
plt.plot(y2_pose,x2_pose,color = 'b',label = "up and down")

plt.legend(loc='upper right')
plt.xlabel("Time")
plt.ylabel("Distance in meters")

plt.show()
