def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# --- CLI Interaction (Add this part below your functions) ---

def main():
    print("Welcome to the Temperature Converter!")
    print("Enter a temperature (e.g., '25C', '77F', '298K'). Type 'exit' to quit.")

    while True:
        user_input = input("Enter temperature: ").strip().upper()

        if user_input == 'EXIT':
            print("Exiting converter. Goodbye!")
            break

        if not user_input or len(user_input) < 2:
            print("Invalid input. Please try again (e.g., '25C').")
            continue

        try:
            value = float(user_input[:-1])
            unit = user_input[-1]

            if unit == 'C':
                fahrenheit = celsius_to_fahrenheit(value)
                kelvin = celsius_to_kelvin(value)
                print(f"{value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K")
            elif unit == 'F':
                celsius = fahrenheit_to_celsius(value)
                kelvin = fahrenheit_to_kelvin(value)
                print(f"{value}°F is {celsius:.2f}°C and {kelvin:.2f}K")
            elif unit == 'K':
                celsius = value - 273.15
                fahrenheit = (celsius * 9/5) + 32
                print(f"{value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F")
            else:
                print("Invalid unit. Please use C, F, or K.")
        except ValueError:
            print("Invalid temperature value. Please enter a number followed by C, F, or K.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

