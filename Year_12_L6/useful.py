import math
from typing import Callable
import dis

class Choice:
    def __init__(self, func: Callable, string: str) -> None:
        self.func = func
        self.string = string

    def inspect(self):
        dis.dis(self.func)

class Chooser:
    def __init__(self):
        self.choices: list[Choice] = []
        self.inspect = False

    def add_choice(self, func: Callable, string: str):
        self.choices.append(Choice(func, string))

    def menu(self):
        choices = self.choices + [Choice(lambda: not self.inspect, "Inspect Mode"), Choice(lambda: exit(), "Exit")] # ensure self.inspect is set properly
        max_length = max([len(i.string) for i in choices])
        
        string = f"Inspect Mode {"ON" if self.inspect else "OFF"}\n"
        string += "'" * ((int(math.log10(len(choices))) + 1) + max_length + 6)
        string += "\n"

        for idx, i in enumerate(choices):
            temp = f"' {str(idx + 1).zfill((int(math.log10(len(choices))) + 1))}. {i.string}"
            string += temp + f"{' '}" * (((int(math.log10(len(choices))) + 1) + max_length + 5) - len(temp)) + "'\n"

        string += "'" * ((int(math.log10(len(choices))) + 1) + max_length + 6)

        string += "\n\nPlease choose which function to run: "
        value = input(string)

        try:
            value = int(value)
        except ValueError:
            print("You didn't give a number.")

        if value > len(choices):
            print("Your number was too big.")
        elif value <= 0:
            print("Your number was too small.")

        if not self.inspect:
            return_value = choices[value - 1].func()
        
        return_value = choices[value - 1].inspect()

        if return_value:
            print(return_value)
        
    def choose(self):
        while True:
            self.menu()