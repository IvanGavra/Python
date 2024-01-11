#from parsers import parse
import random

# Ask the user to enter a lower and an upper bound divided by a comma
#ser_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")

# Parse the user string by calling the parse function




user_input = input("Enter: ")
parse = (user_input.split(","))
#print(parts)
    # Store the two values in variables
lower_bound = int(parse[0])
upper_bound = int(parse[1])

    # Inject the values in a dictionary
parsed = ({"lower_bound": lower_bound, "upper_bound": upper_bound})
print(parsed)
#parsed = parse(user_input)

# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

print(rand)
