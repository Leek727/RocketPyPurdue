import numpy as np
import matplotlib.pyplot as plt
import control

# I1 body
I1 = 0.082

# I2 flywheel
M = 2 # kg
I2 = M * (0.078359 ** 2)

# body A matrix
A = np.array(
    [
        [0,1],
        [0,0]
    ]
)


# body B matrix
B = np.array(
    [
        [0],
        [1/I1]
    ]
)

# initial state
x = np.array([
    [np.pi/2], # body theta
    [10] # body theta dot
], dtype=np.float64)

# torque input
u = 0

# define LQR controller
Q = np.array([
    [100, 0], # penalize position
    [0, 1] # penalize velocity
])
R = np.eye(1) # penalize torque

K, S, E = control.lqr(A, B, Q, R)


setpoint = 0

body_pos = []
body_vel = []

u_int = 0

dt = 0.001
for i in range(10000):
    # append to array
    body_pos.append(x[0][0])
    body_vel.append(x[1][0])

    # update state
    x_dot = A @ x + B * u

    x += x_dot * dt

    e = (setpoint - x[0]) % (2 * np.pi)
    if e > np.pi:
        e -= 2*np.pi
    elif e < -np.pi:
        e += 2*np.pi

    u_int += e * dt
    u_int = np.clip(u_int, -10, 10)

    #u = -K @ x
    S = -np.linalg.inv(R) @ B.T
    S = S @ K
    print(S)
    exit()
    u = S @ x


print(f"Final body speed: {x[-1] * 9.549297}")

plt.plot(body_pos)
plt.title("Body Position")
plt.show()

plt.plot(body_vel)
plt.title("Body Velocity")
plt.show()
