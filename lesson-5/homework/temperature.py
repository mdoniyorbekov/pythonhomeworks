def convert_cel_to_far(celcius: float) -> float:
    return round(celcius*9/5+32,2)
def convert_far_to_cel(fahrenheit:float) ->float:
    return round((fahrenheit-32)*5/9, 2)
def main():
    fahrenheit = float(input("Enter a temperature in degrees Fahrenheit: "))
    celcius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} F = {celcius} degrees C")

    celcius = float(input("\nEnter a temperature in degrees Celcius: "))
    fahrenheit = convert_cel_to_far(celcius)
    print(f"{celcius} C = {fahrenheit} degrees F")
if __name__ == "__main__":
    main()