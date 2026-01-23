

class Ball:

    def __init__(self, position_x, position_y, velocity_at_x, velocity_at_y):
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_at_x = velocity_at_x
        self.velocity_at_y = velocity_at_y

    def update_position_x(self, new_x):
        self.position_x = new_x

    def update_position_y(self, new_y):
        self.position_y = new_y

    def update_velocity_x(self, new_x):
        self.velocity_at_x = new_x

    def update_velocity_y(self, new_y):
        self.velocity_at_y = new_y
    
    # Changes what is output with print
    def __str__(self):
        return f"ball lol \nPosition at X: {self.position_x} \nPosition at Y: {self.position_y} \nVelocity at X: {self.velocity_at_x} \nVelocity at Y: {self.velocity_at_y}"
        


if __name__ == "__main__":
    ball = Ball(0, 0, 0, 0)
    print(ball) # Expected all 0s
    ball.update_position_x(1)
    ball.update_position_y(1)
    ball.update_velocity_x(1)
    ball.update_velocity_y(1)
    print(ball) # Expected all 1s
