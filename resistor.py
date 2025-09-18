# resistor_startere.py
#
# An example of a resistor Class, the Variable Resistors Class code does NoT return the correct information.
# We need to see the result of the percentage applied to the value.

# Tom Kalhous TPRG Fall 2025

class Resistor():
    def__init__(self, value, tol, rating):
        self.value = value
        self.tolerance = tol
        self.rating = rating
        self.voltage = 0.0
        self.current = 0.0
        self.power = 0.0
    def set_voltage(self, volts):
        self.voltage = volts
        self.current = volts / self.value
        self.power = volts**2 / self.value
    def set_current(self, amperes):
        self.voltage = amperes * self.value
        self.current = amperes
        self.power = amperes**2 * self.value
    def parallel(self, other):
        return self.value * other.value / (self.value + other.value)
    def__str__(self):
        return str(self.value) + " " + str(self.tolerance)
    
class VariableResistor(Resistor):
    def__init__(self, value, \
                tol, rating, percent+100):
        super().__init__(value, tol, rating)
        self.percent = percent
        self.real_value = self.value
        self.value = self.real_value * self.percent / 100
    def__str__(self):
        return str(self.real_value) \
               + "@" + str(self.percent) + "%" \
               + " " + str(self.tolerance)
    
if __name__ == "__main__":
    r1 = Resistor(220, 5, 1/4)
    r2 = Resistor(1000, 2, 1/8)
    rv =
    print(r1)
    print(r2)
    print(r3)