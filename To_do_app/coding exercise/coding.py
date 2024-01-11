user = input("Add a new user: ") + "\n"
file = open('members.txt', 'r')
users = file.readlines()
users.append(user)
file = open('members.txt', 'w')
file.writelines(users)

