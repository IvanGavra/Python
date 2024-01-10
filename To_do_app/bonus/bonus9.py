password = input("Enter password: ")
with open('password.txt', 'r') as file:
    pass_frase = password.strip()
    pass_list = file.readlines()
    pass_list.append(pass_frase + '\n')
with open('password.txt', 'w') as file:
    file.writelines(pass_list)

result = {}
if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False
digit = False
for i in password:
    if i.isdigit():
        digit = True
uppercase = False
for x in password:
    if x.isupper():
        uppercase = True
result["upper"] = uppercase
result["digit"] = digit
#print(result)
if all(result.values()) == True:
    print("Strong password")
    with open('password.txt', 'r') as file:
      pass_frase = password.strip()
      pass_list = file.readlines()
      pass_list.append(pass_frase + '\n')
    with open('password.txt', 'w') as file:
      file.writelines(pass_list)
else:
    print("Weak password")

print(result)
