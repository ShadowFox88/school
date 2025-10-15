import random

questions = [
    "Favourite Colour: ",
    "Favourite Animal: ",
    "Favourite Number: ",
    "School House: ",
]

password = ""

while len(questions) != 0:
    question = random.choice(questions)
    questions.remove(question)

    password += input(question).title()
    password += "!"

print("\n\nPassword: " + password)
