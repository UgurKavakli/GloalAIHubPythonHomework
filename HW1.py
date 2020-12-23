# -*- coding: utf-8 -*-

print ("Hello and welcome to my homework\n\nThis is a programme that checks the type of the values you enter so please try entering different types of values")
print("\n")
for i in range(5):
    userInput = input("Please enter a value: ")
    try:
        val = int(userInput)
        inputType = type(val)
        print (f"Your input is {inputType}. Your number= {val}")
    except ValueError:
        try:
            val = float(userInput)
            inputType = type(val)
            print (f"Your input is {inputType}. Your number= {val}")
        except ValueError:
            inputType = type(userInput)
            print(f"Your input is {inputType}. You wrote= {userInput}")