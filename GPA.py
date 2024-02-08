Bangla = float(input("Please enter Your Bangla marks: "))
English = float(input("Please enter Your English marks: "))
Math = float(input("Please enter Your Math marks: "))
Science = float(input("Please enter Your Science marks: "))

avg_gpa = float((Bangla + English + Math + Science) / 4)
print("Average of Marks is ", avg_gpa)

if 90 <= avg_gpa <= 100:
    print("Your grade is A+")
elif 80 <= avg_gpa <= 90:
    print("Your grade is A")
elif 70 <= avg_gpa <= 80:
    print("Your grade is B")
elif 60 <= avg_gpa <= 70:
    print("Your grade is C")
elif 40 <= avg_gpa <= 60:
    print("Your grade is D")
elif 0 <= avg_gpa <= 40:
    print("Your grade is F")
