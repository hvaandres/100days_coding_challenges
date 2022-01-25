# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 90 
lowest_score = 59
medium_score = 70


for scores in student_scores:
  if scores > highest_score:
    print("You are the highest score in class")
  if scores < lowest_score:
    print("You are the lowest score in the class")
  if scores == medium_score:
    print("You have to study to improve your score")
print(scores)

