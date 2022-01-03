# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight / (height) ** 2

if BMI <= 18.4:
  print("You are underweight")
elif BMI <= 24.9:
  print("You're healthy")
elif BMI <= 29.9:
  print("You are over weight")
elif BMI <= 34.9:
  print("You're severely over weight")
elif BMI <= 39.9:
  print("you're obese")

else:
  print("You will have to go to the doctor since you are severely obese")

print(f"you BMI is {BMI}")