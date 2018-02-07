
# coding: utf-8

# In[68]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

grid_size = 10

landmarks = [[grid_size - 1, grid_size - 1], [0, 0]]

def initializeGrid(size):
    x = []
    y = []
    for i in range(size):
        for j in range(size):
            x.append(i)
            y.append(j)
    return [x, y]


class robot:
    
    def __init__(self):
        #self.name = name
        #self.color = color
        self.x = np.random.randint(0,grid_size)
        self.y = np.random.randint(0,grid_size)
        while([self.x, self.y] in [[0,0],[grid_size-1,grid_size-1]]):
            self.x = np.random.randint(0,grid_size)
            self.y = np.random.randint(0,grid_size)   
            
        self.state = 'Resource'
        
        self.sense_noise = 0.0
    
    def set_coordinates(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
    def get_coordinates(self):
        return [self.x, self.y]
    
    def set_noise(self, new_sense_noise):
        self.sense_noise = float(new_sense_noise)
    
    def sense(self):
        z = 0
        
        if self.state == 'Resource':
            dist = sqrt((self.x - landmarks[0][0]) ** 2 + (self.y - landmarks[0][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
        else:
            dist = sqrt((self.x - landmarks[1][0]) ** 2 + (self.y - landmarks[1][1]) ** 2)
            dist += random.gauss(0.0, self.sense_noise)
            
        z = dist
            
        return z
    
    def move(self, step):
        
        x = self.x + step + round(random.gauss(0, 0.5))
        y = self.y + step + round(random.gauss(0, 0.5))

        # cyclic truncate
        x %= grid_size
        y %= grid_size

        # set particle
        res = robot()
        res.set_coordinates(x, y)
        res.set_noise(self.sense_noise)

        return res
    
    @staticmethod
    def gaussian(mu, sigma, x):
        """ calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        :param mu:    distance to the landmark
        :param sigma: standard deviation
        :param x:     distance to the landmark measured by the robot
        :return gaussian value
        """

        # calculates the probability of x for 1-dim Gaussian with mean mu and var. sigma
        return exp(- ((mu - x) ** 2) / (sigma ** 2) / 2.0) / sqrt(2.0 * pi * (sigma ** 2))


    def measurement_prob(self, measurement):
        """ Calculate the measurement probability: how likely a measurement should be
        :param measurement: current measurement
        :return probability
        """

        prob = 1.0

        for i in range(len(landmarks)):
            dist = sqrt((self.x - landmarks[i][0]) ** 2 + (self.y - landmarks[i][1]) ** 2)
            prob *= self.gaussian(dist, self.sense_noise, measurement[i])
        return prob
        

def evaluation(r, p):
    #Calculate the mean error of the system

    sum = 0.0

    for i in range(len(p)):

        # the second part is because of world's cyclicity
        dx = (p[i].x - r.x + (grid_size/2.0)) % grid_size - (grid_size/2.0)
        dy = (p[i].y - r.y + (grid_size/2.0)) % grid_size - (grid_size/2.0)
        err = sqrt(dx**2 + dy**2)
        sum += err

    return sum / float(len(p))

def generateObstacles(size, robots):
    obstaclesX=[]
    obstaclesY=[]
    allCells = size*size
    obstacles = int(allCells/25)
    takenSpaces = [[0,0],[grid_size-1,grid_size-1]]
    for robot in robots:
        takenSpaces.append(robot)
    
    for i in range(obstacles):
        for j in range(obstacles):
            xCoord = np.random.randint(0,grid_size)
            yCoord = np.random.randint(0,grid_size)
            while([xCoord, yCoord] in takenSpaces):
                xCoord = np.random.randint(0,grid_size)
                yCoord = np.random.randint(0,grid_size)
            
            obstaclesX.append(xCoord)
            obstaclesY.append(yCoord)
    return [obstaclesX, obstaclesY]


def getRobotCoordinates(robots, currRobot):
    allRobotCoords=[]
    for robot in robots:
        if(currRobot.get_coordinates() != robot.get_coordinates()):
            allRobotCoords.append(robot.get_coordinates())
    return allRobotCoords


def collision(robot):
    current_pos = robot.get_coordinates()
    if current_pos in getRobotCoordinates(robots, robot):
        robot.set_coordinates(current_pos[0] + random.randint(-1,1) , current_pos[1] - 1)
    
    if current_pos[0] > grid_size:
        robot.set_coordinates(current_pos[0] - 1, current_pos[1] + random.randint(-1,1))
    if current_pos[0] < 0:
        robot.set_coordinates(current_pos[0] + 1, current_pos[1] + random.randint(-1,1))
    if current_pos[1] > grid_size:
        robot.set_coordinates(current_pos[0] + random.randint(-1,1), current_pos[1] - 1)
    if current_pos[1] < 0:
        robot.set_coordinates(current_pos[0] + random.randint(-1,1), current_pos[1] + 1)
        

def visualization(robot):
    #robot2 = robot('r2', 'r')
    myGrid = initializeGrid(grid_size)
    #myObstacles = generateObstacles(gridSize, [robot1.get_coordinates(),robot2.get_coordinates()])
    plt.figure(figsize=(grid_size,grid_size))
    gridPlot = plt.plot(myGrid[0],myGrid[1], 'sy', markersize=20, mfc='none')
    #plt.plot(myObstacles[0],myObstacles[1], '*', markersize=10, color='black')
    plt.plot([robot.get_coordinates()[0]],[robot.get_coordinates()[1]], 'r', marker="$R$", markersize=10)
    #plt.plot([robot2.get_coordinates()[0]],[robot2.get_coordinates()[1]], robot2.color, marker="$R$", markersize=10)
    plt.plot([grid_size-1],[grid_size-1], color="blue", marker="$Res$", markersize=22)
    plt.plot([0],[0], color="blue", marker="$dep$", markersize=22)
    
    plt.show()
    
myrobot = robot()
visualization(myrobot)

myrobot = myrobot.move(1)

visualization(myrobot)
