
# Input a Python list of student heights
student_heights = ["150","158","160"]
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total = 0
for i in student_heights:
  total = total + i 
print(f"total height = {total}")
student =0
for number in student_heights:
  student = student+1
print(f"number of students = {student}")
avg = round(total/student)
print(f"average height = {avg}")



# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")


target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
sum = 0
for number in range(0,target+1,2):
  sum = sum+number
print(sum)


#FizzBuzz
# Write your code here 👇
target = 100
for number in range(1,target+1):
  if number%3==0 and number%5==0:
    print("FizzBuzz")
  elif number%3==0:
    print("Fizz")
  elif number%5==0:
    print("Buzz")
  else:
    print(number)
