import datetime

current_year = datetime.datetime.now().year
my_list = []
def ErrorLine():
    print("\nType Error: Please enter a valid value.")


while True:
    name = input("Please enter your first name: ")
    if (name.isalpha()):
        my_list.append(name)
        break
    else:
        ErrorLine()
        continue

while True:
    surname = input("Please enter your last name: ")
    if (surname.isalpha()):
        my_list.append(surname)
        break
    else:
        ErrorLine()
        continue

while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        ErrorLine()
        continue
    if (age<0):
        ErrorLine()
        continue
    else:
        my_list.append(age)
        break
    
while True:
    try:
        year = int(input("Please enter the year of your birth: "))
    except ValueError:
        ErrorLine()
        continue
    if (year<0):
        ErrorLine()
        continue
    elif(current_year - age != year):
        ErrorLine()
        continue
    else:
        my_list.append(year)
        break
    
print("\n")

for i in my_list:
    print(i)

print("\n")
if (age<18):
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")
