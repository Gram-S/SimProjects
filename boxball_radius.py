import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

class Ball:

    # Set up the ball with initial position and velocity
    def __init__(self, position_x, position_y, velocity_at_x, velocity_at_y, radius):
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_at_x = velocity_at_x
        self.velocity_at_y = velocity_at_y
        self.radius = radius

    # Returns the state as an array [x,y,vx,vy]
    def state(self):
        return np.array([self.position_x, self.position_y, self.velocity_at_x, self.velocity_at_y])
    
    # X is an array [x,y,vx,vy], this is done to make it easier to use euler
    def update_state(self, X):
        self.position_x = X[0]
        self.position_y = X[1]
        self.velocity_at_x = X[2]
        self.velocity_at_y = X[3]


def euler(x, f, dt):
    """
    INPUTS:
        x is an array, in this problem assume it contains [x,y,vx,vy],
            this is the 'state' of the ball
        f is a function, you have written that seperately to encode the
            physics of the ball bouncing in a box.
        dt is the time step for the simulation.
    OUTPUTS:
        an array, corresponding to the updated version of the input x
    """ 
    return x + f(x) * dt


def box_ball(x, radius):
    """
    INPUTS:
        x is an array, in this problem assume it contains [x,y,vx,vy],
            this is the 'state' of the ball
    OUTPUTS:
        an array, it's entries need be constructed such that the constraints of
            the box are observed and the way Euler's method is written in `euler`
            works correctly.
    """
    # Unpack state vector
    pos_x, pos_y, vel_x, vel_y = x

    # Check wall collisions and flip velocities
    # Right wall (x > 1) or Left wall (x < -1)
    if pos_x > 1 - radius or pos_x < -1 + radius:
        x[2] = -vel_x
    # Top wall (y > 1) or Bottom wall (y < -1)
    if pos_y > 1 - radius or pos_y < -1 + radius:
        x[3] = -vel_y

    # Return derivatives: [dx/dt, dy/dt, dvx/dt, dvy/dt]
    # dx/dt = vx, dy/dt = vy, no acceleration so dvx/dt = 0, dvy/dt = 0
    return np.array([x[2], x[3], 0, 0])


if __name__ == "__main__":
    # Initial conditions
    vx = 7
    vy = -8
    x = 0
    y = 0
    x0 = np.array([x,y,vx,vy])
    ball = Ball(x0[0], x0[1], x0[2], x0[3], radius=0.04)

    # Simulation parameters
    dt = 0.001
    end_time = 100

    # Storage for plotting
    X = []
    Y = []

    # Main simulation loop
    t = 0
    while t < end_time:
        # Get current state and store position
        state = ball.state()
        X.append(state[0])
        Y.append(state[1])

        # Update state using euler
        new_state = euler(state, lambda x: box_ball(x, ball.radius), dt)
        ball.update_state(new_state)

        t += dt

    # Plot the results
    # plt.plot([-1,-1,1,1,-1],[-1,1,1,-1,-1],'r')
    # plt.plot(X,Y,'k')
    # plt.show()
    
    ## The following is brought to you by Claude ##
    ### ANIMATION (uses same X, Y data from above) ###
    # Blitting redraws only the ball each frame instead of the whole figure
    fig, ax = plt.subplots()
    ax.plot([-1,-1,1,1,-1], [-1,1,1,-1,-1], 'r')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ball_circle = Circle((X[0], Y[0]), ball.radius, color='blue')
    ax.add_patch(ball_circle)

    def animate(i):
        ball_circle.center = (X[i], Y[i])
        return ball_circle,

    anim = FuncAnimation(fig, animate, frames=len(X), interval=1, blit=True)
    plt.show()