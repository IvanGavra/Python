from To_do_app.projects.project2.func import converter

user_input = input("Enter feet and inches5: ")
user_input = user_input.split()
print(user_input)
feet = float(user_input[0])
inches = float(user_input[1])

print(converter(feet, inches))
