def converter(feet, inches):
    #user_input = input("Enter feet and inches5: ")
    #user_input = user_input.split()
    feet = float(feet)
    inches = float(inches)

    meter = feet * 0.3048 + inches * 0.0254
    meter = round(meter, 2)
    return meter
