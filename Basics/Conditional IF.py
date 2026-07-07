age= int(input("Enter your age: "))

if age > 100:
    print("you are too old ")
elif age <0 :
    print("You are not born yet")
elif age >= 18:
    print("you are signed up")
else:
    print("you must be at least 18 to sign up")


response= input("Would you like food? (Y/N): ")
if response == "Y":
    print("Have some food ")
else:
    print("No food for you")

name= input("Enter your name: ")
if name=="":
    print("You didnt type your name")
else:
    print(f"Your name is {name}")

for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")