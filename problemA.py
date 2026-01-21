# These are neither going to be embedded or passed but rather outside variables because they should never change
import matplotlib.pyplot as plt

room = 0 # Ts
r = 1 # cooling constant
delta = 0.1 # delta t, the "step"
TEMP = 100 # Starting value of temp 

# function
def step(TEMP):
    return TEMP - r * (TEMP - room) * delta # Returns temprature at time t + delta

# Let's try and visualize it:
points = [TEMP]
while TEMP > room+delta:
   TEMP = step(TEMP)
   points.append(TEMP)
    
plt.plot([x * delta for x in range(0, len(points))], points) # first parameter is the time array
plt.ylabel('Temprature')
plt.xlabel('Time')
plt.show()

# print(dTdt
