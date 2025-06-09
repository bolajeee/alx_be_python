# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function to interact with the user
def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        temperature = float(temp_input)

        if unit_input == 'F':
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}F is equal to {celsius:.2f}C")
        elif unit_input == 'C':
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}C is equal to {fahrenheit:.2f}F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
