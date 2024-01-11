name = input("Enter your name: ")
age = int(input("enter your age: "))
year = 2024
cent_year = year + 100

def get_100_older(name, age):
    age_100 = age + 100
    return (f"{name} You will {age_100} in {cent_year} + '\n'")

message = (get_100_older(name,age))
times = int(input("How many time you want to repeat message: "))

def repeting():
    repeat = message * times
    new_line = repeat
    return new_line.split()

print(repeting())
2
