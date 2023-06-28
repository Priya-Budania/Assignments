# case1: take input from user which is student name, roll number, year and percentage
# case2: check if the roll number is unique
# case3: print all students data

students = []
while True:
    name = input("Enter student name: ")
    roll_no = input("Enter student roll no: ")
    year = int(input("Enter student year: "))
    percentage = float(input("Enter student percentage: "))
    if roll_no not in [student['roll_no'] for student in students]:
        students.append({
            'name': name,
            'roll_no': roll_no, 
            'year': year,
              'percentage': percentage})
        print(f"\nStudent {name} added successfully!")
    else:
        print(f"Roll number {roll_no} already exists!")
    choice = input("\nDo you want to add another student? (y/n): ")
    if choice.lower() == 'n':
        break

print("\nAll students data entered:\n")
for student in students:
    print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Year: {student['year']}, Percentage: {student['percentage']}%\n")