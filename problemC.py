import matplotlib.pyplot as plt

def step(T, dt):
    return T - r * (T - Ts) * dt # Returns temperature at time t + delta, i.e. T(t + dt)

r = 0.03
Ts = 17
dt = 0.1

# Add cream first (87 - 5 to 82), cool to 75
temps1 = [87, 82] # Start with initial temp after adding cream
T = 82
while T > 75:
    T = step(T, dt)
    temps1.append(T)
times1 = [0] + [x * dt for x in range(len(temps1)-1)]

# Cool to 80 first, then add cream (80 - 5 to 75)
temps2 = [87]
T = 87
while T > 80:
    T = step(T, dt)
    temps2.append(T)
times2 = [x * dt for x in range(len(temps2))]

temps2.append(temps2[-1] - 5) # Add cream, temp drops by 5 degrees
times2.append(times2[-1])

# Print results, and compare times
print(f"\nCream first: {times1[-1]:.2f} minutes")
print(f"Cream at 80°C: {times2[-1]:.2f} minutes")
print(f"\nCream at 80°C is faster by {times1[-1] - times2[-1]:.2f} minutes")

# Plot cream first
plt.figure()
plt.plot(times1, temps1, 'b-', linewidth=2)
print(temps1)
plt.ylabel('Temperature (°C)')
plt.xlabel('Time (minutes)')
plt.title('Cream first')

# Plot cream at 80°C
plt.figure()
plt.plot(times2, temps2, 'b-', linewidth=2)
plt.ylabel('Temperature (°C)')
plt.xlabel('Time (minutes)')
plt.title('Cream at 80°C')

plt.show()
