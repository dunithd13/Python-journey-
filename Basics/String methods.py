#validate userinput

username= input("Enter a username: ")


if len(username)> 12:
    print("Your username cannot be more than 12 characters")
elif not username.find(" ")== -1:
    print("Your username can't contain spaces" )
elif not username.isalpha():
    print("Your username can't contain numbers")

else:
    print(f"Welcone {username }")







name= input("Enter your full name: ")
#result= len(name)
result = name.find("s")
print(result)

name= name.upper() # convert all the characters to upper case
print(name)

phone_number= input("Enter your number: ")
phone_number= phone_number.replace("-", "")


