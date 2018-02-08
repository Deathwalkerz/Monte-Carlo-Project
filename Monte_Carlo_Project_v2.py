import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

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

class world:
    
    
    def __init__(self, size, region_size):
        self.x=[]
        self.y=[]
        self.grid_color=[]
        self.robot_locations=[]
        for p in range(0,grid_size,subgrid_size):
            for k in range(0,grid_size,subgrid_size):
                for i in range(0+p, 5+p):
                    for j in range(0+k, 5+k):
                        self.x.append(i)
                        self.y.append(j)
        self.robots=["robot()","robot()","robot()"]
        for k in range(len(self.robots)):
            self.robot_locations.append([np.random.randint(0,grid_size),np.random.randint(0,grid_size)])
    def get_grid_color(self, coordinates):
        return self.x
    def get_coordinates(self):
        return [self.x, self.y]