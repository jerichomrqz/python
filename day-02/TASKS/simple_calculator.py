# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.

print ("\nSIMPLE CALCULATOR FOR ALF")

f_num = float(input("Enter the first number: "))
s_num = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")







# Write the code ↓ to perform the calculations based on the selected operation.





if operator == '+':
    ans = f_num + s_num
elif operator == '-':
    ans = f_num - s_num
elif operator == 'x':
    ans = f_num * s_num
elif operator == '/':
    ans = f_num / s_num
else:
    print ("INVALID NUMBER")


 
# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print ("\nThe result of %.1f %s %.1f is %.1f" % (f_num, operator, s_num, and))












