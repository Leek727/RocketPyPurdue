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
env.add_wind_gust(0, 1)

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

#motor.all_info()




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
    inertia=[0.082, 0.082, 11.075],
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


rocket.parachutes = list(parachutes.values())

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

flight.all_info()