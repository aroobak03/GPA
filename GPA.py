def calculate_gpa():
    total_credits = 0
    total_grade_points = 0
    
    num_courses = int(input("Enter the number of courses: "))
    
    for i in range(num_courses):
        course_name = input(f"Enter the name of course #{i+1}: ")
        credit_hours = int(input("Enter the credit hours for this course: "))
        grade = input("Enter the grade for this course (A, B, C, D, F): ")
        
        grade_points = 0
        if grade == "A":
            grade_points = 4.0
        elif grade == "B":
            grade_points = 3.0
        elif grade == "C":
            grade_points = 2.0
        elif grade == "D":
            grade_points = 1.0
        elif grade == "F":
            grade_points = 0.0
        
        course_grade_points = credit_hours * grade_points
        total_grade_points += course_grade_points
        total_credits += credit_hours
    
    gpa = total_grade_points / total_credits
    return gpa

result = calculate_gpa()
print("Your GPA is:", result)
