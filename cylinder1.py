# Student Name- Gurleen Kaur Jassal
#Student ID- 100942372
#Date- 1 November 2024
"""Volume and area of cylinder, with exceptions.
This is the starter version, without exceptions.
The functions return a negative value if the height is negative.

TPRG 2131 Fall 2024 Test 1
"""
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).

from math import pi

def volume_cylinder(diameter, height):
    """
    Calculate the volume of a cylinder given its diameter and height.
    
    Args:
        diameter (float): The diameter of the cylinder's base.
        height (float): The height of the cylinder.
    
    Returns:
        float: The volume of the cylinder.
    
    Raises:
        ValueError: If the height is negative.
    """
    if height < 0:
        raise ValueError("Height must be non-negative")
    return pi * (diameter / 2.0)**2 * height

def area_cylinder(diameter, height):
    """
    Calculate the surface area of a cylinder given its diameter and height.
    
    Args:
        diameter (float): The diameter of the cylinder's base.
        height (float): The height of the cylinder.
    
    Returns:
        float: The surface area of the cylinder.
    
    Raises:
        ValueError: If the height is negative.
    """
    if height < 0:
        raise ValueError("Height must be non-negative")
    radius = diameter / 2.0
    return 2.0 * pi * radius * (height + radius)

if __name__ == "__main__":
    while True:
        try:
            # Prompt user for input
            dia = float(input("\nDiameter? "))
            high = float(input("Height? "))
            
            try:
                # Calculate volume and area
                volume = volume_cylinder(dia, high)
                area = area_cylinder(dia, high)
                
                # Display results
                print(f"The volume is {volume}")
                print(f"The area is {area}")
            except ValueError as e:
                # Handle negative height error
                print(f"Error: {e}. Please enter a positive value for height.")
        except KeyboardInterrupt:
            # Handle program termination (Ctrl+C)
            print("\nGoodbye!")
            break
        except ValueError:
            # Handle invalid input (non-numeric values)
            print("Please enter valid numeric values for diameter and height.")