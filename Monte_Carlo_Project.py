
# coding: utf-8

# In[80]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

gridSize = 25;

def initializeGrid(size):
    x = [];
    y = [];
    for i in range(size):
        for j in range(size):
            x.append(i);
            y.append(j);
    return [x,y]



class robot:
        
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def get_coordinates(self):
        return [self.x, self.y]
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.x = np.random.randint(0,gridSize)
        self.y = np.random.randint(0,gridSize)
    

robot1 = robot('r1', '#000000')
robot2 = robot('r2', 'r')
myGrid = initializeGrid(gridSize)
plt.figure(figsize=(gridSize,gridSize))
gridPlot = plt.plot(myGrid[0],myGrid[1], 'sy', markersize=20, mfc='none')
plt.plot([robot1.get_coordinates()[0]],[robot1.get_coordinates()[1]], robot1.color, marker="$R$", markersize=10)
plt.plot([robot2.get_coordinates()[0]],[robot2.get_coordinates()[1]], robot2.color, marker="$R$", markersize=10)
plt.plot([gridSize-1],[gridSize-1], color="blue", marker="$Res$", markersize=22)
plt.plot([0],[0], color="blue", marker="$dep$", markersize=22)

plt.show()
if([[robot1.get_coordinates()[0]],[robot1.get_coordinates()[1]]] == [[robot2.get_coordinates()[0]],[robot2.get_coordinates()[1]]]):
    print("Robot:" + robot1.name + "Collided with robot:" + robot2.name)


# In[28]:


[[robot1.get_coordinates()[0]],[robot1.get_coordinates()[1]]] == [[robot2.get_coordinates()[0]],[robot2.get_coordinates()[1]]]

