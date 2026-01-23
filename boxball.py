

class Ball:

    def __init__(self, position_x, position_y, velocity_at_x, velocity_at_y):
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_at_x = velocity_at_x
        self.velocity_at_y = velocity_at_y

    # Returns the state as an array [x,y,vx,vy]
    def state(self):
        return [self.position_x, self.position_y, self.velocity_at_x, self.velocity_at_y]
    
    # X is an array [x,y,vx,vy], this is done to make it easier to use euler
    def update_position(self, X):
        self.position_x = X[0]
        self.position_y = X[1]
        self.velocity_at_x = X[2]
        self.velocity_at_y = X[3]
    
    # Switch the velocity in the x direction
    def switch_velocity_x(self):
        self.velocity_at_x = -self.velocity_at_x
    
    # Switch the velocity in the y direction
    def switch_velocity_y(self):
        self.velocity_at_y = -self.velocity_at_y

def euler(x,f,dt):
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

def box_ball(x):
    """
    INPUTS:
        x is an array, in this problem assume it contains [x,y,vx,vy],
            this is the 'state' of the ball
    OUTPUTS:
        an array, it's entries need be constructed such that the constraints of
            the box are observed and the way Euler's method is written in `euler`
            works correctly.
    """
    # TODO: Write this function for a box with sides at x = (-1,1) and y = (-1,1)
    return ''