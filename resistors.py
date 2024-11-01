# Student Name- Gurleen Kaur Jassal
#Student ID- 100942372
#Date- 1 November 2024
""" resistors.py -- Resistors problem for Test 1 
TPRG2131 Fall 202x Test 1
"""
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).
class Resistor(object):
    """Model a fixed resistor."""
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms."""
        self.resistance = res

    def current(self, voltage):
        """Given a voltage across the resistor, return the current."""
        return voltage / self.resistance

    def __str__(self):
        """Return a string representation of the resistor."""
        return "R=" + str(self.resistance)

class VariableResistor(Resistor):
    """Model a variable resistor."""
    def __init__(self, res):
        """
        Constructor sets the fixed resistance and initializes actual resistance.
        
        Args:
            res (float): The maximum resistance value in ohms.
        """
        super().__init__(res)
        self.actual_resistance = res

    def set_resistance(self, percent):
        """
        Set the actual resistance based on a percentage from 0 to 100.
        
        Args:
            percent (float): The percentage of maximum resistance to set.
        
        Raises:
            ValueError: If the percentage is not between 0 and 100.
        """
        if 0 <= percent <= 100:
            self.actual_resistance = (percent / 100) * self.resistance
        else:
            raise ValueError('Percentage must be between 0 and 100')

    def current(self, voltage):
        """
        Given a voltage across the variable resistor, return the current based on actual resistance.
        
        Args:
            voltage (float): The voltage across the resistor.
        
        Returns:
            float: The current flowing through the resistor.
        """
        return voltage / self.actual_resistance

if __name__ == "__main__":
    # Create a fixed resistor with 1000 ohms
    r1 = Resistor(1000.0)
    print("R1:", r1)
    print("R1: voltage=12.0, current=", r1.current(12.0))

    # Create a variable resistor with maximum 1000 ohms
    r2 = VariableResistor(1000.0)
    print("R2:", r2)
    print("R2 100%: voltage=12.0, current=", r2.current(12.0))
    
    # Set the variable resistor to 50% of its maximum resistance
    r2.set_resistance(50.0)
    print("R2 50%: voltage=12.0, current=", r2.current(12.0))