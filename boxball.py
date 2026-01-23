import numpy as np
import matplotlib.pylab as plt

class Ball:

    def __init__(self, position_x, position_y, velocity_at_x, velocity_at_y):
        self.name = self
        self.state_vector = np.array([position_x, position_y, velocity_at_x, velocity_at_y])

    def euler_update_all(self, function, time_step):
        self.state_vector =  self.state_vector + function(self.state_vector) * time_step
        
    # Changes what is output with print
    def __str__(self):
        return f"\nball lol \n[x y vx vy]\n{self.state_vector}"
        


if __name__ == "__main__":
    ball = Ball(1, 1, 1, 1)

    # Test function adds 1 to everything
    def test_function(array):
        for i in range(array.size):
            array[i] += 1
        return array

    ball.euler_update_all(test_function, 0.1)
    print(ball) # Expected 4.4,4.4,3.3,3.3
