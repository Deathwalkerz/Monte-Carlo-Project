
# coding: utf-8

# In[140]:

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
        for i in range(sample_size):
            sample_coords = [np.random.randint(0, grid_size), np.random.randint(0, grid_size)]
            self.sample.append(sample_coords)
        
        
    
    def sense(self, world, robo_index):
        robots = world.get_robot_locations()
        colors = world.get_grid_color()
        robot = robots[robo_index]
        robo_color = colors[robot[0]][robot[1]]
        for sample in self.sample:
            if robo_color == colors[int(sample[0])][int(sample[1])]:
                self.weights.append(0.9)
            else:
                self.weights.append(0.1)
        
        self.weights = np.divide(self.weights, sum(self.weights))
        
        
    def resample(self):
        new_sample = []
        new_sample.append(np.random.choice([row[0] for row in self.sample], len(self.sample), p=self.weights))
        new_sample.append(np.random.choice([row[1] for row in self.sample], len(self.sample), p=self.weights))
        self.sample = new_sample
        return self.sample
        
        
    def policy(self):
        
        x_sum = 0
        y_sum = 0
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
        self.robots=[robot(),robot(),robot()]
        for k in range(len(self.robots)):
            self.robot_locations.append([np.random.randint(0,grid_size),np.random.randint(0,grid_size)])
            
    def get_grid_color(self):
        return self.grid_colors
    
    def get_coordinates(self):
        return [self.x, self.y]
    
    def update_moves(self):
        for index, loc in enumerate(self.robot_locations):
            self.robot_locations[index] = [self.robot_locations[index][0] + self.robots[index].policy()[0], self.robot_locations[index][1] + self.robots[index].policy()[1]]             + [round(random.gauss(0, 0.5)), round(random.gauss(0, 0.5))]
        
            self.robot_locations[index][0] %= grid_size
            self.robot_locations[index][1] %= grid_size
    
    def get_robot_locations(self):
        return self.robot_locations   
        
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
            
            

        
        
                
                
fig = plt.figure(figsize=(grid_size,grid_size))
ax = plt.axes()
plt.plot(grid_coords[0],grid_coords[1], 'sy', markersize=20, mfc='none')


for i in range(grid_size):
    for j in range(grid_size):
        plt.plot(i, j, 'sy', markersize=20, mfc=('none' if coords[i][j] == "B" else '#d3d3d3'))
              
def animate(i):
    number_string = str(i).zfill(len(str(20)))
    
    for index, robot in enumerate(myWorld.robots):
        robot.sense(myWorld, index)
        robot.resample()
        myWorld.update_moves()
        
    r1 = plt.plot([myWorld.robot_locations[0][0]],[myWorld.robot_locations[0][1]], 'r', marker="$R$", markersize=10) 
    r2 = plt.plot([myWorld.robot_locations[1][0]],[myWorld.robot_locations[1][1]], 'r', marker="$R$", markersize=10) 
    r3 = plt.plot([myWorld.robot_locations[2][0]],[myWorld.robot_locations[2][1]], 'r', marker="$R$", markersize=10) 
    
    ax.set_title('t = ' + number_string)
    return r1, r2 , r3

ani = animation.FuncAnimation(fig, animate, 20)     
   
plt.axis('off')        
plt.show()


# In[4]:




# In[3]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
get_ipython().magic('matplotlib')
fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
                              interval=25, blit=True)
plt.show()


# In[6]:

class osem:
    def __init__(self):
        self.asd = [1,2,3]
        
edno = osem()        
print(edno.asd)


# In[20]:

import numpy as np
print(np.round(5*np.random.random_sample((10, 2))), type(np.rint(5*np.random.random_sample((10, 2))[1][1])))


for counter, value in enumerate(['a','n','c']):
    print(counter, value)


# In[113]:

a = np.round(20 * np.random.random_sample((10, 2)))

for row in a:
    print(a[row][0])


# In[107]:

np.divide([2,3,5], 5)

