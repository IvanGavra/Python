waiting_list = ["sen", "ben", "john"]
waiting_list.sort()
for i, x in enumerate(waiting_list):
    row = f"{i + 1}.{x.capitalize()}"
    print(row)
waiting_list.sort(reverse=True)
print(waiting_list)
filenames = ['documet', 'report', 'presentation']
for i, j in enumerate(filenames):
    print(f"{i}-{j}")
