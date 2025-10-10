import math
from typing import Callable

class Choice:
    def __init__(self, func: Callable, string: str) -> None:
        self.func = func
        self.string = string

class Chooser:
    def __init__(self):
        self.choices: list[Choice] = []

    def add_choice(self, func: Callable, string: str):
        self.choices.append(Choice(func, string))

    def choose(self):
        choices = self.choices + [Choice(lambda: None, "Exit")]
        max_length = max([len(i.string) for i in choices])
        
        string = "'" * ((int(math.log10(len(choices))) + 1) + max_length + 6)
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

        return_value = choices[value - 1].func()

        if return_value:
            print(return_value)
        
