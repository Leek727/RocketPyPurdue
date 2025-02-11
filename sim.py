from rocketpy import (
    Environment,
    SolidMotor,
    Rocket,
    Flight,
    TrapezoidalFins,
    EllipticalFins,
    RailButtons,
    NoseCone,
    Tail,
    Parachute,
)
import datetime


env = Environment()
env.set_location(latitude=28.61, longitude=-80.6)
env.set_elevation(0.0)

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
env.set_date((tomorrow.year, tomorrow.month, tomorrow.day, 12))
# env.set_atmospheric_model(type='Forecast', file='GFS')
#env.add_wind_gust(0, 1)

#env.all_info()

motor = SolidMotor(
    thrust_source="theseus/thrust_source.csv",
    dry_mass=0,
    center_of_dry_mass_position=0,
    dry_inertia=[0, 0, 0],
    grains_center_of_mass_position=0,
    grain_number=1,
    grain_density=971.6200215930797,
    grain_outer_radius=0.049,
    grain_initial_inner_radius=0.0245,
    grain_initial_height=0.751,
    grain_separation=0,
    nozzle_radius=0.036750000000000005,
    nozzle_position=-0.3755,
    throat_radius=0.0245,
    reshape_thrust_curve=False,  # Not implemented in Rocket-Serializer
    interpolation_method="linear",
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

#print(motor.all_info())




nosecone = NoseCone(
    length=0.78359,
    kind="ogive",
    base_radius=0.078359,
    rocket_radius=0.078359,
    name="0.78359",
)


trapezoidal_fins = {}

trapezoidal_fins[0] = TrapezoidalFins(
    n=4,
    root_chord=0.1397,
    tip_chord=0.1397,
    span=0.12446,
    cant_angle=0.0,
    sweep_length=0.038099999999999995,
    sweep_angle=None,
    rocket_radius=0.078359,
    name="Fin - L Brackets",
)

trapezoidal_fins[1] = TrapezoidalFins(
    n=4,
    root_chord=0.254,
    tip_chord=0.254,
    span=0.0254,
    cant_angle=0.0,
    sweep_length=0.0,
    sweep_angle=None,
    rocket_radius=0.078359,
    name="Trapezoidal Fin Set",
)

tails = {}

tails[0] = Tail(
    top_radius=0.078359,
    bottom_radius= 0.07619999999999999,
    length=0.0254,
    rocket_radius=0.078359,
    name='FG-Al Joint',
)


tails[1] = Tail(
    top_radius=0.07619999999999999,
    bottom_radius= 0.078359,
    length=0.0254,
    rocket_radius=0.078359,
    name='FG-Al Joint',
)


tails[2] = Tail(
    top_radius=0.078359,
    bottom_radius= 0.07619999999999999,
    length=0.0254,
    rocket_radius=0.078359,
    name='FG-Al Joint',
)

# remove fins
#trapezoidal_fins = {}
#tails = []




parachutes = {}

parachutes[0] = Parachute(
    name="Light HP Parachute [Cd 2.2 (10.4 oz) 34.62 in^3]",
    cd_s=16.052,
    trigger=304.800,
    sampling_rate=100,
)

parachutes[1] = Parachute(
    name="Pro X Drogue Parachute [Cd .97 (8.5 oz) 28.27 in^3]",
    cd_s=1.769,
    trigger="apogee",
    sampling_rate=100,
)

rocket = Rocket(
    radius=0.078359,
    mass=20.797,
    inertia=[11.075,11.075,0.082],
    power_off_drag="theseus/drag_curve.csv",
    power_on_drag="theseus/drag_curve.csv",
    center_of_mass_without_motor=1.761,
    coordinate_system_orientation="nose_to_tail",
)

rocket.add_surfaces(
    surfaces=[
        nosecone,
        trapezoidal_fins[0],
        trapezoidal_fins[1],
        tails[0],
        tails[1],
        tails[2],
    ],
    positions=[
        0.0,
        3.1894780000000003,
        3.214878,
        1.6160750000000004,
        1.6160750000000004,
        1.6160750000000004,
    ],
)
rocket.add_motor(motor, position=2.364803294573643)


rocket.parachutes = []#list(parachutes.values())

rail_buttons = rocket.set_rail_buttons(
    upper_button_position=2.350,
    lower_button_position=2.727,
    angular_position=0.000,
)


flight = Flight(
    rocket=rocket,
    environment=env,
    rail_length=1.0,
    inclination=90.0,
    heading=90.0,
    terminate_on_apogee=False,
    max_time=600,
)

print(f"Apogee x: {flight.apogee_x}\nApogee y: {flight.apogee_y}")
print(flight.all_info())

#print(rocket.evaluate_dry_inertias())
print(flight.w3())
# 18 in, 7 lbs
# TODO 3 DOF, axes of rotation, rocket control system demo by end of next semester

# 0.038812405990997285 rad/s^2
"""
time_to_apogee_ork = 24.186
time_to_apogee_rpy = flight.apogee_time
print(f"Time to apogee (OpenRocket): {time_to_apogee_ork:.3f} s")
print(f"Time to apogee (RocketPy):   {time_to_apogee_rpy:.3f} s")
apogee_difference = time_to_apogee_rpy - time_to_apogee_ork
error = abs((apogee_difference) / time_to_apogee_rpy) * 100
print(f"Time to apogee difference:   {error:.3f} %")
print()

flight_time_ork = 299.717
flight_time_rpy = flight.t_final
print(f"Flight time (OpenRocket): {flight_time_ork:.3f} s")
print(f"Flight time (RocketPy):   {flight_time_rpy:.3f} s")
flight_time_difference = flight_time_rpy - flight_time_ork
error_flight_time = abs((flight_time_difference) / flight_time_rpy) * 100
print(f"Flight time difference:   {error_flight_time:.3f} %")
print()

ground_hit_velocity_ork = -4.364
ground_hit_velocity_rpy = flight.impact_velocity
print(f"Ground hit velocity (OpenRocket): {ground_hit_velocity_ork:.3f} m/s")
print(f"Ground hit velocity (RocketPy):   {ground_hit_velocity_rpy:.3f} m/s")
ground_hit_velocity_difference = ground_hit_velocity_rpy - ground_hit_velocity_ork
error_ground_hit_velocity = (
    abs((ground_hit_velocity_difference) / ground_hit_velocity_rpy) * 100
)
print(f"Ground hit velocity difference:   {error_ground_hit_velocity:.3f} %")
print()

launch_rod_velocity_ork = 20.759
launch_rod_velocity_rpy = flight.out_of_rail_velocity
print(f"Launch rod velocity (OpenRocket): {launch_rod_velocity_ork:.3f} m/s")
print(f"Launch rod velocity (RocketPy):   {launch_rod_velocity_rpy:.3f} m/s")
launch_rod_velocity_difference = launch_rod_velocity_rpy - launch_rod_velocity_ork
error_launch_rod_velocity = (
    abs((launch_rod_velocity_difference) / launch_rod_velocity_rpy) * 100
)
print(f"Launch rod velocity difference:   {error_launch_rod_velocity:.3f} %")
print()

max_acceleration_ork = 293.004
max_acceleration_rpy = flight.max_acceleration
print(f"Max acceleration (OpenRocket): {max_acceleration_ork:.3f} m/s²")
print(f"Max acceleration (RocketPy):   {max_acceleration_rpy:.3f} m/s²")
max_acceleration_difference = max_acceleration_rpy - max_acceleration_ork
error_max_acceleration = abs((max_acceleration_difference) / max_acceleration_rpy) * 100
print(f"Max acceleration difference:   {error_max_acceleration:.3f} %")
print()

max_altitude_ork = 3397.777
max_altitude_rpy = flight.apogee - flight.env.elevation
print(f"Max altitude (OpenRocket): {max_altitude_ork:.3f} m")
print(f"Max altitude (RocketPy):   {max_altitude_rpy:.3f} m")
max_altitude_difference = max_altitude_rpy - max_altitude_ork
error_max_altitude = abs((max_altitude_difference) / max_altitude_rpy) * 100
print(f"Max altitude difference:   {error_max_altitude:.3f} %")
print()

max_mach_ork = 1.123
max_mach_rpy = flight.max_mach_number
print(f"Max Mach (OpenRocket): {max_mach_ork:.3f}")
print(f"Max Mach (RocketPy):   {max_mach_rpy:.3f}")
max_mach_difference = max_mach_rpy - max_mach_ork
error_max_mach = abs((max_mach_difference) / max_mach_rpy) * 100
print(f"Max Mach difference:   {error_max_mach:.3f} %")
print()

max_velocity_ork = 380.956
max_velocity_rpy = flight.max_speed
print(f"Max velocity (OpenRocket): {max_velocity_ork:.3f} m/s")
print(f"Max velocity (RocketPy):   {max_velocity_rpy:.3f} m/s")
max_velocity_difference = max_velocity_rpy - max_velocity_ork
error_max_velocity = abs((max_velocity_difference) / max_velocity_rpy) * 100
print(f"Max velocity difference:   {error_max_velocity:.3f} %")
print()

max_thrust_ork = 7095.311
max_thrust_rpy = flight.rocket.motor.thrust.max
print(f"Max thrust (OpenRocket): {max_thrust_ork:.3f} N")
print(f"Max thrust (RocketPy):   {max_thrust_rpy:.3f} N")
max_thrust_difference = max_thrust_rpy - max_thrust_ork
error_max_thrust = abs((max_thrust_difference) / max_thrust_rpy) * 100
print(f"Max thrust difference:   {error_max_thrust:.3f} %")
print()

burnout_stability_margin_ork = 2.403
burnout_stability_margin_rpy = flight.stability_margin(
    flight.rocket.motor.burn_out_time
)
print(f"Burnout stability margin (OpenRocket): {burnout_stability_margin_ork:.3f}")
print(f"Burnout stability margin (RocketPy):   {burnout_stability_margin_rpy:.3f}")
burnout_stability_margin_difference = (
    burnout_stability_margin_rpy - burnout_stability_margin_ork
)
error_burnout_stability_margin = (
    abs((burnout_stability_margin_difference) / burnout_stability_margin_rpy) * 100
)
print(f"Burnout stability margin difference:   {error_burnout_stability_margin:.3f} %")
print()

max_stability_margin_ork = 2.529
max_stability_margin_rpy = flight.max_stability_margin
print(f"Max stability margin (OpenRocket): {max_stability_margin_ork:.3f}")
print(f"Max stability margin (RocketPy):   {max_stability_margin_rpy:.3f}")
max_stability_margin_difference = max_stability_margin_rpy - max_stability_margin_ork
error_max_stability_margin = (
    abs((max_stability_margin_difference) / max_stability_margin_rpy) * 100
)
print(f"Max stability margin difference:   {error_max_stability_margin:.3f} %")
print()

min_stability_margin_ork = 0.0
min_stability_margin_rpy = flight.min_stability_margin
print(f"Min stability margin (OpenRocket): {min_stability_margin_ork:.3f}")
print(f"Min stability margin (RocketPy):   {min_stability_margin_rpy:.3f}")
min_stability_margin_difference = min_stability_margin_rpy - min_stability_margin_ork
error_min_stability_margin = (
    abs((min_stability_margin_difference) / min_stability_margin_rpy) * 100
)
print(f"Min stability margin difference:   {error_min_stability_margin:.3f} %")
print()

"""