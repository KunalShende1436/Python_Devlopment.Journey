math = int(input("Enter marks in Math="))
science = int(input("Enter marks in Science="))
english = int(input("Enter marks in English="))

total = math + science + english
percentage = (total / 300) * 100
print(
    f"Student Scored {math}in Math ,{science} in Science and {english} in English with total marks {total} and percentage {percentage:.2f}%"
)
