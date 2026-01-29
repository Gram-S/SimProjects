import numpy as np
import matplotlib.pyplot as plt
import math

def Euler(dt, f, t, y, *args):
    return y + f(t,y,args) * dt

def solve_ode(f, tspan, y0, method = Euler, *args, **options):

    y = [ y0[0] ] # Vector with initial position
    t = [ tspan[0] ] # Vector with initial time

    dt = 0.01 # Let some dt value be pretty low

    while t[-1] < tspan[1]:
        solved_value = method(dt, f, t[-1], y[-1], args)
        y.append(solved_value)
        t.append(t[-1] + dt)

    y = np.array(y)
    t = np.array(t)
    return t, y


if __name__ == "__main__":

    def simple_gravity(t, y, g):
        return y - g[0][0]*t

    g = 9.8
    y = [3, 0]
    t = [0, math.sqrt(6/g)]
    print(solve_ode(simple_gravity, t, y, Euler, 9.8))