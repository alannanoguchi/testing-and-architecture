# By Kami Bigdely
# Remove assignment to method parameter.
class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

    def convert_ly_to_km(self):
        km_conversion = 9.461e12
        
        if self.unit == "km":
            return self.value
        elif self.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit        
            self.value = self.value * km_conversion
            self.unit = "km"
            return self.value
        else:
            print ("unit is Unknown")

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def convert_mass_to_kg(self):
        solar_mass_conversion = 1.98892e30

        if self.unit == 'kg':
            return self.value
        elif self.unit == "solar-mass":
            self.value = self.value * solar_mass_conversion
            self.unit = "kg"
            return self.value
        else:
            print ("unit is Unknown")
            return


def calculate_kinetic_energy(mass, distance, time):
    distance.convert_ly_to_km()
    mass.convert_mass_to_kg()

    speed = distance.value/time # [km per sec]    
    kinetic_energy = 0.5 * mass.value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))