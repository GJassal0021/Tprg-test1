# Student Name- Gurleen Kaur Jassal
#Student ID- 100942372
#Date- 1 November 2024
"""Volume and area of cylinder, with exceptions.
This is the starter version, without exceptions.
The functions return a negative value if the height is negative.

TPRG 2131 Fall 202x Test 1
"""
# This program is strictly my own work. Any material
# beyond course learning materials that is taken from
# the Web or other sources is properly cited, giving
# credit to the original author(s).



import pytest
from cylinder import volume_cylinder, area_cylinder

@pytest.mark.parametrize("diameter, height, expected_volume", [
    (1, 2, 1.5708),
    (0.1, 4, 3.1416E-02),
    (2, 1, 3.1416)
])
def test_volume_cylinder(diameter, height, expected_volume):
    """
    Test the volume_cylinder function with various inputs.
    
    This test checks if the calculated volume matches the expected volume
    for different combinations of diameter and height.
    """
    assert round(volume_cylinder(diameter, height), 4) == expected_volume

@pytest.mark.parametrize("diameter, height, expected_area", [
    (1, 2, 7.8540),
    (0.1, 4, 1.2723),
    (2, 1, 12.5664)
])
def test_area_cylinder(diameter, height, expected_area):
    """
    Test the area_cylinder function with various inputs.
    
    This test checks if the calculated surface area matches the expected area
    for different combinations of diameter and height.
    """
    assert round(area_cylinder(diameter, height), 4) == expected_area

def test_volume_cylinder_negative_height():
    """
    Test that volume_cylinder raises a ValueError for negative height.
    
    This test ensures that the function properly handles invalid input
    by raising a ValueError when given a negative height.
    """
    with pytest.raises(ValueError):
        volume_cylinder(1, -1)

def test_area_cylinder_negative_height():
    """
    Test that area_cylinder raises a ValueError for negative height.
    
    This test ensures that the function properly handles invalid input
    by raising a ValueError when given a negative height.
    """
    with pytest.raises(ValueError):
        area_cylinder(1, -1)        