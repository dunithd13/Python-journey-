# Format specifier = {f: flags} format a value based on what flags are inserted

# .(number)f= round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03= allocate and zero pad that many spaces
# :< = left justify

price1 = 3.14159
price2= -987.65
price3= 12.34

print(f"price 1 is {price1: .3f}") # colan for format classifier, 2f means 2 decimal points
print(f"price 2 is {price2: .2f}")
print(f"Price 3 is {price3: 1}")