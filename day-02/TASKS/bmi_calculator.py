# BMI - NUTRITIONAL STATUS GUIDE
"""
    BMI         NUTRITIONAL STATUS

BELOW 18.5         UNDERWEIGHT
18.5 - 24.9       NORMAL WEIGHT
25.0 - 29.9        OVERWEIGHT
ABOVE 30.0          OBESITY
"""
 
# Write the code ↓ to read user's height and weight.
# Be cautious when reading input of various data types.

print ("\nBMI CALCULATOR FOR ALF")

weight = float(input("\nEnter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))







# Write the code ↓ to perform the calculations of user's BMI and categorize its status.




bmi = weight / (height ** 2)

if bmi < 18.5:
    result = "UNDERWEIGHT"
elif bmi < 24.9:
    result = "NORMAL WEIGHT"
elif bmi < 29.9:
    result = "OVERWEIGHT"
elif bmi < 30.0:
    result = "OBESITY"


# Write the code ↓ to display the user's BMI and its classification.
# Select and employ a string concatenation method based on your personal preference and comfort level.
# Use :.2f format specifier when printing the BMI value to display the BMI with only two decimal places.







print ("\nHEIGHT: %.2f - WEIGHT: %.2f" %(height, weight))
print ("BMI: %.2f - NUTRITIONAL STATUS: %s" %(bmi, result)) 
