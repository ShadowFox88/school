code = input()

valid = True

if len(code) != 6:
    valid = False
if not code[0].isdigit():
    valid = False
if not code[-1].isdigit():
    valid = False
if " " in code:
    valid = False
if code[1].isdigit() or code[2].isdigit() or code[3].isdigit() or code[4].isdigit():
    valid = False

print("valid" if valid else "invalid")