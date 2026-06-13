marks = int(input("Enter your marks:"))
grade = (
    "A"
    if marks >= 90
    else "B" if marks >= 80 else "C" if marks >= 70 else "D" if marks >= 60 else "F"
)
print(f"Your marks is {marks} and your grade is {grade}")
