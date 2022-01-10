print("Welcome to the rollercoaster!")

height = int(input("What is your heigh in cm?\n"))

if height >= 12:
  print("You can get a rite in the rollercoaster")
  age = int(input("What is your age?\n"))
  if age <= 12:
    print("Please pay $10.00")
  elif age >= 18:
    print("Please pay $20.00")
  else:
    print("Please pay 5.00")
else:
  print("Sorry, you have to be taller before you can join us")

