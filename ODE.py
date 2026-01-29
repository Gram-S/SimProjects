import numpy as np
import matplotlib.pyplot as plt
import math

def Euler(dt, f, t, y, args):
    return y + f(t,y,*args) * dt 

def EulerCromer():
    # TODO: Write this consistent with formulas.
    pass

def EulerRichardson():
    # TODO: Write this consistent with formulas.
    pass


def solve_ode(f,tspan, y0, method = Euler, *args, **options):
    """
    Given a function f that returns derivatives,
    dy / dt = f(t, y)
    and an inital state:
    y(tspan[0]) = y0
    
    This function will return the set of intermediate states of y
    from t0 (tspan[0]) to tf (tspan[1])
    
    
    
    The function is called as follows:
    
    INPUTS 
    
    f - the function handle to the function that returns derivatives of the 
        vector y at time t. The function can also accept parameters that are
        passed via *args, eg f(t,y,g) could accept the acceleration due to gravity.
        
    tspan - a indexed data type that has [t0 tf] as its two members. 
            t0 is the initial time
            tf is the final time
    
    y0 - The initial state of the system, must be passed as a numpy array. I think it is [starting postion (y0), init velocity]
    
    method - The method of integrating the ODEs. This week will be one of Euler, 
             Euler-Cromer, or Euler-Richardson
    
    *args - extra positional arguments that become a tuple containing 
        additional parameters you would like for the function handle f.
    
    **options - keyword arguments that become a dictionary containing 
                the keywords that might be used to control function behavior. 
                For now, there is only one:
                
                first_step - the initial time step for the simulation.
    
    
    OUTPUTS
    
    t,y
    
    The returned states will be in the form of a numpy array
    t containing the times the ODEs were solved at and an array
    y with shape tsteps,N_y where tsteps is the number of steps 
    and N_y is the number of equations
    
    """
    steps = 0
    y=[ y0[0] ] # Initial Position 
    t=[ tspan[0] ] # Initial time
    dt = 0.1 # Assume some timestep to be small

    if method not in (Euler,EulerCromer,EulerRichardson):
        raise Error("wrong")

    while t[-1] < tspan[1]:
        steps += 1
        y.append([steps, method(dt, f, t[-1], y[-1], args)])
        t.append(t[-1]+dt)

    y = np.array(y)
    t = np.array(t)
    print(y, "\n", t)
    return t, y # We know this has to be the return
    
if __name__ == "__main__":

    
    # y = [y,v]
    def simple_gravity(t,y,g):
        dydt = y # Velocity v
        dvdt = -g
        print(y, g)
        return dydt * dvdt

    print(solve_ode(simple_gravity, [0,10], [0,0], Euler, 9.8)) # Should return -9.8
    

    # TODO: Write the code that initializes the lists to hold y and t,
    # sets the initial conditions and time step, checks that the method is known,
    # then loops over all time steps to get the updated states and times, placing
    # them in lists. Finally, return the arrays specified in the function's documentation, 
    # above.
    
