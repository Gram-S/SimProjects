import matplotlib.pyplot as plt

def step(T, dt):
    return T - r * (T - Ts) * dt # Returns temprature at time t + delta

# Set parameters for part (a)
r = 1
Ts = 0
dt = 0.1
T0 = 100

# Run simulation, storing results in lists
temps = [T0]
T = T0
t = 0

while T > Ts + 0.01:
    T = step(T, dt)
    t = t + dt
    temps.append(T)
    
times = [x * dt for x in range(len(temps))]

# Plot temps and times
plt.plot(times, temps, 'b-', linewidth=2)
plt.ylabel('Temperature (°C)')
plt.xlabel('Time')
plt.show()