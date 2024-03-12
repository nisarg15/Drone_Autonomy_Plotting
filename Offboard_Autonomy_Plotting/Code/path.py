# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 18:04:14 2023

@author: Enigma
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import axes3d


path = pd.read_csv('C:/Users/nisar/Downloads/path_2 .csv')


x_pose = path["x_pose"]
y_pose = path["y_pose"]
z_pose = path["z_pose"]

x_pose = np.array(x_pose)
y_pose = np.array(y_pose)
z_pose = np.array(z_pose)

ax = plt.axes(projection = "3d")

ax.scatter(x_pose,y_pose,z_pose,color='r')
ax.set_title('path of the drone')
ax.set_xlabel('x direction')
ax.set_ylabel('y direction')
ax.set_zlabel('z direction')

plt.show()


