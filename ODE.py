import numpy as np
import matplotlib.pyplot as plt
import math
%matplotlib inline

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
    
    y0 - The initial state of the system, must be passed as a numpy array.
    
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
    y=[y0]
    t=[tspan[0]]

    if method not in (Euler,EulerCromer,EulerRichardson):
        raise Error("wrong")

    while t[-1] < tspan[1]:
        y.append()
    
if __name__ == "__main__":

    # y = [y,v]
    def simple_gravity(t,y,g):
        dydt = y[1] # Velocity v
        dvdt = -g
        return dydt, dvdt

    y = [3, 0]
    t = [0, math.sqrt(6/g)]
   #  print(solve_ode(simply_gravity, [t0,tf], [y0,v0], Euler)) # Should return -9.8
    

    # TODO: Write the code that initializes the lists to hold y and t,
    # sets the initial conditions and time step, checks that the method is known,
    # then loops over all time steps to get the updated states and times, placing
    # them in lists. Finally, return the arrays specified in the function's documentation, 
    # above.
    
