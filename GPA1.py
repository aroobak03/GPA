import streamlit as st

def calculate_gpa():
    total_credits = 0
    total_grade_points = 0

    num_courses = st.number_input("Enter the number of courses:", min_value=1, value=1, step=1)

    for i in range(num_courses):
        course_name = st.text_input(f"Enter the name of course #{i+1}:")
        credit_hours = st.number_input("Enter the credit hours for this course:", min_value=1, value=3, step=1)
        grade = st.selectbox("Select the grade for this course:", ("A", "B", "C", "D", "F"))

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

    if total_credits == 0:
        return 0

    gpa = total_grade_points / total_credits
    return gpa

def main():
    st.title("GPA Calculator")
    gpa = calculate_gpa()
    st.write("Your GPA is:", gpa)

if __name__ == "__main__":
    main()