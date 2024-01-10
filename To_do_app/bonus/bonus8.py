date = input("Enter todays date: ")
mood = input("How do yu rate your modd today: ")
journal = input("let's your thoughts flow:\n ")
with open(f'./journal/{date}.txt', 'w') as file:
    file.write(mood)
    file.write(journal)
