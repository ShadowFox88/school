from useful import Chooser

def getMonth(month: int):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    return months[month - 1]

def getAge():
    dob = input("Enter DOB in the form DD/MM/YYYY: ").split("/")
    year = int(input("Enter the year you want to check the age for: "))

    print(f"You will be {year - int(dob[2])} on {dob[0]} {getMonth(int(dob[1]))} {dob[2]}")

c = Chooser()
c.add_choice(getAge, "Get age")

c.choose()