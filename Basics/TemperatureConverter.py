unit = input("Is this temperature celcius or fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5+32,1)
    print(f"temperature is in fahrenheit is: {temp} F ")
elif unit == "F":
    temp = round((temp-32)*5 /9,1)
    print(f"Temperature in celcius is: {temp} C ")
else:
    print(f"{unit} is an invalid option")