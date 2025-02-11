import numpy as np

torque = ""
with open("rocketpy/simulation/torque.txt", "r") as f:
    torque = float(f.read())

def getControlMoments(u):
    """Returns moments in all three axes given the state vector -> [M1, M2, M3] where M3 is z through nosecone

    Units: m, rad/s
    u = [x, y, z, vx, vy, vz, e0, e1, e2, e3, omega1, omega2, omega3].
    """
    #                                                roll angular vel
    x, y, z, vx, vy, vz, e0, e1, e2, e3, omega1, omega2, omega3 = u
    rps = 100
    #torque = 2.379 * 0.07835 # 2.379N * .07835m
    #return [0,0,300]

    #print(20*(2*np.pi*rps-omega3))
    max_force = 2 #N
    out_diameter = .152 # m
    radius = out_diameter / 2 # m
    max_moment = radius * max_force
    
    control_moment = 20*(2*np.pi*rps-omega3)
    if (abs(control_moment) > max_moment):
        control_moment = np.sign(control_moment) * max_moment
    
    
    return [1,0,0]


    #return [0,0,0]

"""


Torque 0
Apogee x: 2.920279437412893e-09
Apogee y: -115.44731210161979
Torque 1
Apogee x: 0.9652350375533756
Apogee y: -115.23910285960396
Torque 2
Apogee x: 1.7330513022533875
Apogee y: -115.01003577801033
Torque 3
Apogee x: 2.4065009211085777
Apogee y: -114.77757664613772
Torque 4
Apogee x: 3.0374943346116656
Apogee y: -114.53552675999421
Torque 5
Apogee x: 3.6247768981587494
Apogee y: -114.30109804063804
Torque 6
Apogee x: 4.188884303161789
Apogee y: -114.08212524604977
Torque 7
Apogee x: 4.714109608545447
Apogee y: -113.84560605428508
Torque 8
Apogee x: 5.2304018122873925
Apogee y: -113.60860558308669
Torque 9
Apogee x: 5.724564518325001
Apogee y: -113.3928014629728
"""