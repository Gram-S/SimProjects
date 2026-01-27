import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
from ball import Ball

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
    x0 = np.array([x, y, vx, vy])
    ball = Ball(x0[0], x0[1], x0[2], x0[3], radius=0.04)

    # Simulation parameters
    dt = 0.001
    end_time = 100

    # Storage for plotting

    # Main simulation loop
    t = 0
    while t < end_time:
        # Get current state and store position
        ball.add_to_memory()

        # Update state using euler
        new_state = euler(ball.state(), lambda x: box_ball(x, ball.radius), dt)
        ball.update_state(new_state)

        t += dt

        # Plot the results
        # plt.plot([-1,-1,1,1,-1],[-1,1,1,-1,-1],'r')
        # plt.plot(X,Y,'k')
        # plt.show()

        ## The following is brought to you by Claude ##
        ### ANIMATION (uses same X, Y data from above) ###
        # Blitting redraws only the ball each frame instead of the whole figure
    # Set up the inital box
    fig, ax = plt.subplots()
    box = patches.Rectangle((-1, -1), 2, 2, edgecolor='red', facecolor='none')
    ax.add_patch(box)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect("equal")
        
    anim = ball.animate(fig, ax)
    plt.show()
