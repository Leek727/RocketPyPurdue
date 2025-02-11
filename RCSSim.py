import numpy as np
import matplotlib.pyplot as plt

# I1 body
I1 = 0.082

# I2 flywheel
M = 2 # kg
I2 = M * (0.078359 ** 2)

# body A matrix
A = np.array(
    [
        [0,0,1,0],
        [0,0,0,1],
        [0,0,0,0],
        [0,0,0,0]
    ]
)

# body B matrix
B = np.array(
    [
        0,
        0,
        -1/I1,
        1/I2
    ]
)

# initial state
x = np.array([
    100, # body theta
    0, # flywheel theta
    0, # body theta dot
    0 # flywheel theta dot
], dtype=np.float64)

# torque input
u = 0


v1 = []
v2 = []

# PID for kP,  kI, kD
kP = .5
kI = 0
kD = 1.5

setpoint = np.pi

dt = 0.001
for i in range(10000):
    x_dot = A @ x + B * u
    x += x_dot * dt
    v1.append((x[0]))# % (2 * np.pi)) - np.pi) # body theta

    
    #print(f"Body theta: {x[0]}")
    e = (setpoint - x[0]) % (2 * np.pi)
    if e > np.pi:
        e -= 2*np.pi
    elif e < -np.pi:
        e += 2*np.pi

    uo = kP * e + kD * x[2]
    u = np.clip(uo, -10, 10)
    #rint(f"Control: {u}, Control raw: {uo}")
    # plot flywheel speed
    #v2.append(x[3])
    #print(f"Control: {u}")


plt.plot(v1)
#plt.plot(v2)
plt.show()