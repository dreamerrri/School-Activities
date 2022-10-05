# A Program that will ask for the number of class held and numbers class attended by the student.
# Computes for the percentage of class attendance and displays the result.
# Determines if the student is allowed take the exam or not. 

Cls = float(input("Enter number of classes held: "))
Atn = float(input("Enter number of classes attended by the student: "))

Avg = (Atn / Cls) * 100

if Avg > 75:
    print(" ")
    print("Attendance percentage is:", Avg)
    print("You are allowed to take exam")
else:
    print(" ")
    print("Attendance percentage is:", Avg)
    print("Sorry you are not allowed. Attend more classes from next time")
