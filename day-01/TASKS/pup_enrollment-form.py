# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.

print ("\nPUP Enrollment Form")


fullName = input ("\nEnter your full name: ")
age = int (input("Enter your age: "))
gwa = float(input("Enter your previous general weighted average: "))
member = input("Are you a member of the AWS Cloud Club - Department of Cloud Computing? (yes/no): ").lower() == "yes"



# Write the code ↓ to display the user's personal information.
# Select and employ a string concatenation method based on your personal preference and comfort level.


print ("\nYour Enrollment Form")
print ("Name: " + fullName)
print ("Age: ", age)
print ("GWA: ", gwa)
print ("Awstraunot: ", member)




