import json


with open('questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question['alternatives']):
        print(index + 1, "-",  alternative)
    user_choise = int(input("Enter your answer: "))
    question["user_choice"] = user_choise

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    message = f'{index + 1 } {result}  Your answer: {question["user_choice"]}, correct answer: {question["correct_answer"]}'
    print(message)
#print(data)
#print(score, '/', len(data))
