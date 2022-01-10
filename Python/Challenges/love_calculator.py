# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# We have to combine the names to do the calculation
combined_names = name1 + name2

#We have to have everything in lower case
lower_case_string = combined_names.lower()

# The calculation will be base on true and love. How many times we are repeating the letters on the names

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e


# to get the love, we will have to count letter by letter under the string of the two words

love_score = int(str(true) + str(love))

# loops to help to see what would it be the best score

if (love_score < 10) or (love_score > 90):
  print(f"Your score is {love_score} , you go together like coke and mentos.")

elif (love_score >= 40) and (love_score <=50):
  print(f"Your score is {love_score}, you are alright together")

else:
  print(f"Your score is {love_score}")