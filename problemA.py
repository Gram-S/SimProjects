# These are neither going to be embedded or passed but rather outside variables because they should never change
ROOM = 0 # Ts
R = 1 # cooling constant

# dTdt = -R * (TEMP - ROOM)
# print(dTdt)

# function
def step(TEMP, DELTA):
    return TEMP - R * (TEMP - ROOM) * DELTA

temp = 100
dt = 0.1
print("Starting temp", temp)
print("Temp after", dt, "step", step(temp, dt))
