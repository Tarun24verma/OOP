def length(value, from_unit, to_unit):
    """
    Convert a length value from one unit to another.

    Parameters:
    - value: The numerical value to convert.
    - from_unit: The unit of the input value (e.g., 'meters', 'feet').
    - to_unit: The unit to convert the value to (e.g., 'inches', 'kilometers').

    Returns:
    - The converted value in the specified unit.
    """
    # Define conversion factors relative to meters
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }

    # Check if the units are valid
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Invalid units provided for conversion.")

    # Convert the input value to meters
    value_in_meters = value * conversion_factors[from_unit]

    # Convert from meters to the target unit
    converted_value = value_in_meters / conversion_factors[to_unit]

    return converted_value
if __name__ == "__main__":
    # Example usage
    print(length(1, 'meters', 'feet'))        # Convert 1 meter to feet
    print(length(100, 'centimeters', 'inches'))  # Convert 100 centimeters to inches
    print(length(5, 'miles', 'kilometers'))   # Convert 5 miles to kilometers