def temperature(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert temperature from one unit to another.

    Parameters:
    value (float): The temperature value to convert.
    from_unit (str): The unit of the input temperature ('C', 'F', 'K').
    to_unit (str): The unit to convert the temperature to ('C', 'F', 'K').

    Returns:
    float: The converted temperature value.
    """
    if from_unit == to_unit:
        return value

    # Convert from the source unit to Celsius
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    else:
        raise ValueError("Invalid from_unit. Use 'C', 'F', or 'K'.")

    # Convert from Celsius to the target unit
    if to_unit == 'C':
        return celsius
    elif to_unit == 'F':
        return (celsius * 9/5) + 32
    elif to_unit == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Invalid to_unit. Use 'C', 'F', or 'K'.")

if __name__ == "__main__":
    # Example usage
    print(temperature(100, 'C', 'F'))  # Convert 100°C to Fahrenheit
    print(temperature(32, 'F', 'C'))   # Convert 32°F to Celsius
    print(temperature(0, 'C', 'K'))     # Convert 0°C to Kelvin 