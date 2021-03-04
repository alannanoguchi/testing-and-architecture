# def calculate_kinetic_energy(mass, velocity): 
#     """Returns kinetic energy of mass [kg] with velocity [ms]."""
#     return 0.5 * mass * velocity ** 2

# Example of a failed test 
def calculate_kinetic_energy(mass, velocity): 
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return mass * velocity ** 2

def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 160