# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# adding a variable for the price
pizza_price = 0

# Loop to see what is the size + price of the pizza
if size == "S":
  pizza_price += 15
elif size == "M":
  pizza_price += 20
else:
  pizza_price += 25

# Loop to see if the client will be adding pepperoni to their pizza
if add_pepperoni == "Y":
  if size == "S":
    pizza_price += 2
  else:
    pizza_price += 3

# Loop to see if the client will be adding Cheese to their pizza
if extra_cheese == "Y":
  pizza_price += 1

# Adding the last print statement to know the total of your pizza

print(f"The total price of your pizza would be {pizza_price}")

  


  
  
    


  
  
  
  




