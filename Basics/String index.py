#indexing = accessing elements of a sequence using [] (indexing operation)
#  [start : end : step]

credit_no = "1234-5678-9012-3456"
print(credit_no[0])

print(credit_no[0:4])

print(credit_no[5:9])

print(credit_no[5:])  # prints from 5th index to end

print(credit_no[-1])  # prints the last

# build a program to get last 4 numbers of credit card number

credit= "1234-5678-9012-3456"

last_digits= credit[-4:]
print(f"xxxx-xxxx-xxxx-{last_digits}")

# reverse the characters of credit card number
credit= credit[::-1]
print(credit)