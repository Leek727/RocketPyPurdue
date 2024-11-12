import os

for i in range(0, 10):
    x = i * 10
    with open("rocketpy/simulation/torque.txt", "w") as f:
        f.write(str(x))

    print(f"Angular velocity {x} rps")
    os.system('python sim.py')