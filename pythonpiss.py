import tkinter as tk

root = tk.Tk()






def fahrenheit_to_celsius(fahrenheit):
    """Converts a temperature value from Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    """Converts a temperature value from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Prompt the user to choose which conversion they want to perform
print("Select a conversion:")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = input("Enter 1 or 2: ")

# Perform the chosen conversion
if choice == "1":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is {celsius} degrees Celsius.")
elif choice == "2":
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is {fahrenheit} degrees Fahrenheit.")
else:
    print("Invalid choice. Please enter 1 or 2.")


root.mainloop()