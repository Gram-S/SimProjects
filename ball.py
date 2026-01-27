import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

class Ball:
    # Set up the ball with initial position and velocity
    def __init__(self, position_x, position_y, velocity_at_x, velocity_at_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_at_x = velocity_at_x
        self.velocity_at_y = velocity_at_y
        self.radius = radius
        self.x_memory = []
        self.y_memory = []

    def add_to_memory(self):
        self.x_memory.append(self.position_x)
        self.y_memory.append(self.position_y)

    def get_x_memory(self):
        return self.x_memory

    def get_y_memory(self):
        return self.y_memory

    # Returns the state as an array [x,y,vx,vy]
    def state(self):
        return np.array([self.position_x, self.position_y, self.velocity_at_x, self.velocity_at_y])

    # Plots the path the ball took
    def plot(self, plot):
        plot.plot(self.x_memory, self.y_memory, "k")

    # pass in two subplots from plt.subplots()
    def animate(self, figure, axis):        
        ball_circle = patches.Circle((self.x_memory[0], self.y_memory[0]), self.radius, color="blue")
        axis.add_patch(ball_circle)
        
        def animate(i):
            ball_circle.center = (self.x_memory[i], self.y_memory[i])
            return (ball_circle,)
        
        return FuncAnimation(figure, animate, frames = len(self.x_memory), interval = 1, blit = True)

    # X is an array [x,y,vx,vy], this is done to make it easier to use euler
    def update_state(self, X):
        self.position_x = X[0]
        self.position_y = X[1]
        self.velocity_at_x = X[2]
        self.velocity_at_y = X[3]
