import numpy as np
import matplotlib.pylab as plt
from ball import Ball
# probably not needed in the jyupter notebook

class Box:

    def __init__(self, bounds_x, bounds_y):
        self.bounds_x = bounds_x
        self.bounds_y = bounds_y

    def __str__(self):
        return f"\nbox lol\n X bounds: {self.bounds_x}\n Y bounds: {self.bounds_y}"


def euler_input_function(boxes):
    pass
    

# Test client
if __name__ == "__main__":
    # Test import
    ball_test = Ball(1,1,1,1)
    print(ball_test)

    box_test = Box(range(-1,1), range(-1,1))
    print(box_test)
