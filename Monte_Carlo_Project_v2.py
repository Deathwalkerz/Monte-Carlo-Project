
# coding: utf-8

# In[3]:

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
        self.sample = []
        self.weights = []
        
        
    
    def sense(self, coords):
        
        
        
    def resample(self):
        new = np.random.choice(self.sample, 5, p=[0.5, 0.1, 0.1, 0.3])
        self.sample = new
        return new
        
    def policy(self):
    

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
                
plt.figure(figsize=(grid_size,grid_size))
plt.plot(grid_coords[0],grid_coords[1], 'sy', markersize=20, mfc='none')
for i in range(grid_size):
    for j in range(grid_size):
        plt.plot(i, j, 'sy', markersize=20, mfc=('none' if coords[i][j] == "B" else '#d3d3d3'))
        
plt.axis('off')        
plt.show()


# In[16]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
get_ipython().magic('matplotlib')

N = 15
# make an empty data set
data = np.ones((N, N)) * np.nan
# fill in some fake data
for j in range(3)[::-1]:
    data[N//2 - j : N//2 + j +1, N//2 - j : N//2 + j +1] = j
# make a figure + axes
fig, ax = plt.subplots(1, 1, tight_layout=True)
# make color map
my_cmap = matplotlib.colors.ListedColormap(['r', 'g', 'b'])
# set the 'bad' values (nan) to be white and transparent
my_cmap.set_bad(color='w', alpha=0)
# draw the grid
for x in range(N + 1):
    ax.axhline(x, lw=2, color='k', zorder=5)
    ax.axvline(x, lw=2, color='k', zorder=5)
# draw the boxes
ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
# turn off the axis labels
ax.axis('off')

