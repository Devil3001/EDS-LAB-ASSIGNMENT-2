marks = []
for i in range(5):
    marks.append(int(input(f"Enter marks of subject {i+1}: ")))

if min(marks) < 40:
    print("Result: Fail")
else:
    total = sum(marks)
    percentage = total / 5

    print("Result: Pass")
    print("Percentage:", percentage)

    if percentage > 75:
        print("Grade: Distinction")
    elif percentage >= 60:
        print("Grade: First Division")
    elif percentage >= 50:
        print("Grade: Second Division")
    else:
        print("Grade: Third Division")

