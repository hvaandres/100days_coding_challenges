#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = int(input("How much is your total?\n"))
people = int(input("Are you splitting the bill? If so, tell me how many people?\n"))
tip = int(input("How much you will leave as a tip? [Popular tips = 10 / 12 / 15%]\n"))

total = round(bill * (1 + tip/100), 2)
share = round(total / people, 2)

print("Each person will pay ${} from the total of ${}.".format(share, total))