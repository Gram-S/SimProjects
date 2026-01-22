import matplotlib.pyplot as plt

def step(T, dt):
    return T - r * (T - Ts) * dt # Returns temprature at time t + delta, i.e. T(t + dt)

# Set parameters for part (b)
r = 0.03 # r must have units of 1/min, since time is in minutes. So r=0.03 corresponds to 30 per hour
Ts = 17
T0 = 87

### Make sure that your value of delta t is sufficiently small so that it does not affect your results
# 0.1 appears to be sufficiently small
dt = 0.1
times = [0]
temps = [T0]
T = T0
t = 0

while T > Ts + 0.01:
    T = step(T, dt)
    t = t + dt
    temps.append(T)
    times.append(t)

# Plot times and temps
plt.plot(times, temps, 'b-', linewidth=2)
plt.ylabel('Temperature (°C)')
plt.xlabel('Time')
plt.show()