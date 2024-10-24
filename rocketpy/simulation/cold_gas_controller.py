def getControlMoments(u):
    """Returns moments in all three axes given the state vector -> [M1, M2, M3] where M3 is z through nosecone

    u = [x, y, z, vx, vy, vz, e0, e1, e2, e3, omega1, omega2, omega3].
    """
    #                                                roll angular vel
    x, y, z, vx, vy, vz, e0, e1, e2, e3, omega1, omega2, omega3 = u
    return [0,0,2000*(100-omega3)]

"""
No spin
Apogee X position: 0.000 m
Apogee Y position: -115.447 m

Spin 100
Apogee X position: 21.076 m
Apogee Y position: 3.924 m
"""