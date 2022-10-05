# Determines if a student passed the Semester.
# A program that will ask for the name of the student, grade for Math, grade for Science, Grade for English.
# Computes for the average grade.
# Determines if the student  passed the semester. (4points)
# -if average is equal or more than 75, the student passed the semester. Otherwise failed.
# -also determines if the students has a back subject.
# Could use some work and optimization.

Name = input("Enter Student Name: ")
Math = float(input("Enter Math Grade: "))
Science = float(input("Enter Science Grade: "))
English = float(input("Enter English Grade: "))

Avg = (Math + Science + English) / 3

if Avg >= 75 and Math >= 75 and Science >= 75 and English >= 75:
    print(" ")
    print(Name, "Congratulations! You passed the semester.")
else:
    if Avg >= 75 and Math < 75 and Science >= 75 and English >= 75:
        print(" ")
        print(Name, "Congratulations! You passed the semester, But you need to re-enroll in Math.")
    elif Avg >= 75 and Math >= 75 and Science < 75 and English >= 75:
        print(" ")
        print(Name, "Congratulations! You passed the semester, But you need to re-enroll in Science.")
    elif Avg >= 75 and Math >= 75 and Science >= 75 and English < 75:
        print(" ")
        print(Name, "Congratulations! You passed the semester, But you need to re-enroll in English.")
    else:
        print(" ")
        print("Sorry, you failed the semester.")
