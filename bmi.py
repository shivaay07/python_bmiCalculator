import math
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line
print(f"your height is {height}m\nyour weight is {weight}kg")
height= float(height)
weight = float(weight)
height_in_feet=int((height*39.37)/12)
height_in_inches=round((height*39.37)%12)
print(f"{height_in_feet} feet and {height_in_inches} inches")
bmi=round(weight/(height**2))
print(f"your BMI is {bmi}")
