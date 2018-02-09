import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

#%matplotlib

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

class sample:
    def __init__(self):
        self.coordinates = [np.random.randint(0, grid_size), np.random.randint(0, grid_size)]
        
    def set_coorditnates(self, coordinates):
        self.coordinates = coordinates
        
    def get_coordinates(self):
        return self.coordinates

class robot:
    
    def __init__(self):
        self.particles = []
        self.weights = []
        for i in range(sample_size):
            #sample_coords = [np.random.randint(0, grid_size), np.random.randint(0, grid_size)]
            #mySample.set_coorditnates(sample_coords)
            self.particles.append(sample())
            self.weights.append(1/sample_size)
        
        
    
    def sense(self, world, robo_index):
        robots = world.get_robot_locations()
        colors = world.get_grid_color()
        robot = robots[robo_index]
        robo_color = colors[robot[0]][robot[1]]
        for sample_i, sample_ in enumerate(self.particles):
            print("Iteration: ", sample_i)
            print("For a robot: ", sample_.get_coordinates())
            print("Particles length: ", len(self.particles))
            if robo_color == colors[sample_.get_coordinates()[0]][sample_.get_coordinates()[1]]:
                self.weights[sample_i] = 0.9
            else:
                self.weights[sample_i] = 0.1
        print("Loop ended. Weights: ", self.weights)
        self.weights = np.divide(self.weights, sum(self.weights))
        
        
    def resample(self):
        new_sample = []
        print("Old sample:", self.particles)
        
        new_sample=np.random.choice(a=self.particles,size=len(self.particles),replace=False, p=self.weights)
        self.particles = new_sample
        print("New sample:", self.particles)
        return self.particles
        
        
    def policy(self):
        
        x_sum = 0
        y_sum = 0
        for part in self.particles:
            x_sum += part.get_coordinates()[0]
            y_sum += part.get_coordinates()[1]
        return [int(x_sum/(2*len(self.particles))), int(y_sum/(2*len(self.particles)))]
    

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
            self.robot_locations[index][0] = self.robot_locations[index][0] + self.robots[index].policy()[0] + round(random.gauss(0, 1))
            self.robot_locations[index][1] = self.robot_locations[index][1] + self.robots[index].policy()[1] + round(random.gauss(0, 1))
            self.robot_locations[index][0] %= grid_size
            self.robot_locations[index][1] %= grid_size
    
    def get_robot_locations(self):
        return self.robot_locations   
        
myWorld = world(grid_size, subgrid_size)
grid_coords=myWorld.get_coordinates()
coords = myWorld.get_grid_color()

            

fig = plt.figure(figsize=(grid_size,grid_size))
ax = plt.axes()
plt.plot(grid_coords[0],grid_coords[1], 'sy', markersize=20, mfc='none')
rob_plots=[]
for i in range(grid_size):
    for j in range(grid_size):
        plt.plot(i, j, 'sy', markersize=20, mfc=('none' if coords[i][j] == "B" else '#d3d3d3'))

def plot_init():

    #r1 = plt.plot(myWorld.get_robot_locations()[0][0],myWorld.robot_locations[0][1], '#000000', marker="$R$", markersize=10) 
    #r2 = plt.plot(myWorld.get_robot_locations()[1][0],myWorld.robot_locations[1][1], '#0800ff', marker="$R$", markersize=10) 
    #r3 = plt.plot(myWorld.get_robot_locations()[2][0],myWorld.robot_locations[2][1], '#ff0000', marker="$R$", markersize=10) 

    for i in range(len(myWorld.robots)):
        circle = plt.Circle((myWorld.get_robot_locations()[i][0],myWorld.robot_locations[i][1]),radius=0.4,fc='r')
        rob_plots.append(circle)
        ax.add_patch(circle)
    
    return rob_plots

              
def animate(frame):
    number_string = str(frame).zfill(len(str(200)))
    for index, robot in enumerate(myWorld.robots):
        robot.sense(myWorld, index)
        robot.resample()
        
    print(frame)
    myWorld.update_moves()
    

    for index, robo in enumerate(rob_plots):
        robo.center = (myWorld.get_robot_locations()[index][0], myWorld.get_robot_locations()[index][1])

    

    #r1 = plt.plot(myWorld.get_robot_locations()[0][0],myWorld.robot_locations[0][1], '#000000', marker="$R$", markersize=10) 
    #r2 = plt.plot(myWorld.get_robot_locations()[1][0],myWorld.robot_locations[1][1], '#0800ff', marker="$R$", markersize=10) 
    #r3 = plt.plot(myWorld.get_robot_locations()[2][0],myWorld.robot_locations[2][1], '#ff0000', marker="$R$", markersize=10) 
    
    ax.set_title('t = ' + number_string)
    return rob_plots

ani = animation.FuncAnimation(fig, animate, init_func=plot_init, frames=200,interval=1000, blit=True)  

    
plt.axis('off')
plt.show()
