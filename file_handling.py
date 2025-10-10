from useful import Chooser

def add_character():
    name = input("Enter the character's name: ")
    health = input("Enter the character's health: ")
    stamina = input("Enter the character's stamina: ")
    hunger = input("Enter the character's hunger: ")

    with open("characters.txt", "a") as f:
        f.write(f"\n{name}\n{health}\n{stamina}\n{hunger}")
        
def read_character():
    name = input("Enter the character's name: ")

    with open("characters.txt", "r") as f:
        data = [i.strip() for i in f.readlines()]
        
    for idx, i in enumerate(data):
        if idx % 4 == 0:
            if i == name:
                print(f"{name}\nHealth: {data[idx + 1]}\nStamina: {data[idx + 2]}\nHunger: {data[idx + 3]}")
    
c = Chooser()
c.add_choice(add_character, "Add Character")
c.add_choice(read_character, "Read Character")

c.choose()