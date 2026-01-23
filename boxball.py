

class Ball:

    def __init__(self, position_x, position_y, velocity_at_x, velocity_at_y):
        self.name = self
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_at_x = velocity_at_x
        self.velocity_at_y = velocity_at_y

    def update_position_x(self, new_x):
        self.position_x = new_x

    def update_position_y(self, new_y):
        self.position_y = new_y

    def change_velocity_x(self, multiplier_for_x):
        self.velocity_at_x *= multiplier_for_x

    def change_velocity_y(self, multiplier_for_y):
        self.velocity_at_y = multiplier_for_y
    
    # Changes what is output with print
    def __str__(self):
        return f"""
        ball lol 
        Position at X: {self.position_x} 
        Position at Y: {self.position_y} 
        Velocity at X: {self.velocity_at_x} 
        Velocity at Y: {self.velocity_at_y}
        """
        


if __name__ == "__main__":
    ball = Ball(1, 1, 1, 1)
    print(ball) # Expected all 1s
    ball.update_position_x(0)
    ball.update_position_y(0)
    ball.change_velocity_x(-1)
    ball.change_velocity_y(-1)
    print(ball) # Expected 0,0,-1,-1
