def converter(feet, inches):
    meter = float(feet) * 0.3048 + float(inches) * 0.0254
    return round(meter, 2)


if __name__ == "__main__":
    converter(5, 6)

# print(converter(5,6))
