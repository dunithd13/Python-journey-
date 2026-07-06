# Process of converting a variable from one data type to another

name= "Dunith Desitha"
age= 23
gpa =3.7
is_Student= True

print(type(name))

print(type(gpa))
#convert gpa into integer
gpa=int(gpa)

print(gpa)

age=float(age)
print(age)

#input function in python

school= input("What is your school ?: ")

print(f"you are from {school} ")

#Exercise 1
#calculating area of rectangle

length=float(input("Enter length"))
width= float(input("Enter width"))

area=length*width

print(f" Area is: {area} cm")
