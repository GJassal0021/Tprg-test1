# Student Name- Gurleen Kaur Jassal
#Student ID- 100942372
#Date- 1 November 2024
"""TPRG2131 Winter 2024 RC class starter with simplistic test code."""
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

import math

class ResistorCapacitor(object):
    """Model a resistor-capacitor network"""
    def __init__(self, resistance, capacitance, initial=0.0):
        """Initialize the resistor-capacitor network with resistance, capacitance, and initial voltage."""
        self.resistance = resistance  # Resistance in ohms
        self.capacitance = capacitance  # Capacitance in farads
        self.initial_voltage = initial  # Initial voltage across the capacitor

    def set_voltage(self, voltage):
        """Set the voltage."""
        self.initial_voltage = voltage  # Set the initial voltage to the provided value

    def voltage(self, time):
        """Calculate the voltage across the capacitor over time based on the RC charging equation."""
        tau = self.resistance * self.capacitance  # Time constant
        return self.initial_voltage * (1 - math.exp(-time / tau))  # Voltage over time based on RC formula

# Test code (place at bottom of the file)
if __name__ == "__main__":
    print("Self testing...")
    rc1 = ResistorCapacitor(1000.0, 1.0e-6)
    rc1.set_voltage(5.0)
    rc2 = ResistorCapacitor(10.0e3, 22.0e-6, 12.0)
    print("rc1:")
    print(rc1.resistance, rc1.capacitance, rc1.initial_voltage)
    for vtime in range(0, 6):
        stime = vtime * 0.5e-3
        print(stime, rc1.voltage(stime))
    print("rc2:")
    print(rc2.resistance, rc2.capacitance, rc2.initial_voltage)
    for vtime in range(0, 6):
        stime = vtime * 150.0e-3
        print(stime, rc2.voltage(stime))
