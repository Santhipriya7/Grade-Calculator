name = input("Enter student name: ")
Telugu = int(input("Enter marks for Telugu: "))
Hindi = int(input("Enter marks for Hindi: "))
English = int(input("Enter marks for English: "))
Maths = int (input("Enter marks for Maths: "))
Science = int (input("Enter marks for Science: "))
Social = int(input("Enter marks for Social: "))
totalmarks = Telugu + Hindi + English  + Maths + Science + Social 
average = totalmarks / 5
if 90 <= average <= 100:
    grade = "A"
elif 80 <= average <= 90:
    grade  = "B"
elif 70 <= average <80:
    grade = "C"
elif 60 <= average <= 70:
    grade = "D"
else:
    grade = "F"
print("Student Name: ",name)
print("totalmarks: " , totalmarks)
print("average: ", average)
print("grade: ", grade)

