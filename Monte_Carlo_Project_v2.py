
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

sample_size = 10
grid_size = 20
subgrid_size = int(grid_size/4)

def split(arr, size):
    arrs = []
    while(len(arr) > size):
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs


class robot:
    
    def __init__(self):
        self.sample = grid_size * np.random.random_sample((sample_size, 2))
        self.weights = []
        
        
    
    #def sense(self, coords):
        
        
        
    def resample(self):
        new_sample = np.random.choice(self.sample, len(self.sample), p=self.weights)
        self.sample = new_sample
        return self.sample
        
        
    def policy(self):
        for part in self.sample:
            x_sum += part[0]
            y_sum += part[1]
        return [int(x_sum/(2*len(self.sample))), int(y_sum/(2*len(self.sample)))]
    

class world:
    
    def __init__(self, size, region_size):
        self.x=[]
        self.y=[]
        self.grid_colors=[[0 for x in range(grid_size)] for y in range(grid_size)]
        self.robot_locations=[]
        for p in range(0,grid_size,subgrid_size):
            for k in range(0,grid_size,subgrid_size):
                choose_color = np.random.randint(0,2)
                for i in range(0+p, 5+p):
                    for j in range(0+k, 5+k):
                        self.x.append(i)
                        self.y.append(j)
                        self.grid_colors[i][j]= "W" if choose_color == 0 else "B"
        self.robots=["robot()","robot()","robot()"]
        for k in range(len(self.robots)):
            self.robot_locations.append([np.random.randint(0,grid_size),np.random.randint(0,grid_size)])
            
    def get_grid_color(self):
        return self.grid_colors
    
    def get_coordinates(self):
        return [self.x, self.y]

    
myWorld = world(grid_size, subgrid_size)
grid_coords=myWorld.get_coordinates()
coords = myWorld.get_grid_color()
coords[9][19]
c=[]
d=[]
s=[[0 for x in range(grid_size)] for y in range(grid_size)]

for p in range(0,grid_size,subgrid_size):
    for k in range(0,grid_size,subgrid_size):
        choose_color = np.random.randint(0,2)
        for i in range(0+p, 5+p):
            for j in range(0+k, 5+k):
                c.append(i)
                d.append(j)
                s[i][j]= "W" if choose_color == 0 else "B"
            
            
def update_moves():
    for index, loc in enumerate(robot_locations):
        robot_locations[i] =  [robot_locations[i][0] + myWorld.robots[index].policy, robot_locations[i][1] + myWorldrobots[index].policy]         + [round(random.gauss(0, 0.5)), round(random.gauss(0, 0.5))]                 
                
                
plt.figure(figsize=(grid_size,grid_size))
plt.plot(grid_coords[0],grid_coords[1], 'sy', markersize=20, mfc='none')
for i in range(grid_size):
    for j in range(grid_size):
        plt.plot(i, j, 'sy', markersize=20, mfc=('none' if coords[i][j] == "B" else '#d3d3d3'))
        
        
        
plt.axis('off')        
plt.show()
