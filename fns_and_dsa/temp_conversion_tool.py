# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9  # Conversion factor from Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5  # Conversion factor from Celsius to Fahrenheit
FAHRENHEIT_OFFSET = 32  # Offset for Fahrenheit to Celsius conversion

# Function to Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - FAHRENHEIT_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_OFFSET

# Main function to interact with the user
def main():
    try:
        # User input: Temperature and unit (Celsius or Fahrenheit)
        temp_input = input("Enter the temperature value: ")
        unit_input = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

        # Validate input: Check if temperature is numeric
        temperature = float(temp_input)

        # Perform conversion based on the unit entered
        if unit_input == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {celsius:.2f}°C")
        elif unit_input == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {fahrenheit:.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
