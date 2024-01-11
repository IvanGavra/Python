try:
    width = float(input("Enter widht: "))
    lenght = float(input("Enter lenght: "))
    if width == lenght:
        exit("That's looks like a square")
    area = width * lenght
    print(area)
except ValueError:
    print("Please enter a number.")

