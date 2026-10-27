gpa = 4.2
is_active_in_student_council = False
has_volunteer_experience = True
scholarship_type = ""

if gpa >= 4.5 and is_active_in_student_council:
  scholarship_type = "full"
elif gpa >= 4.0 or has_volunteer_experience:
  scholarship_type = "partial"
elif not (
    (gpa >= 4.5 and is_active_in_student_council)
    or (gpa >= 4.0 or has_volunteer_experience)
):
  scholarship_type = "no"

print(
    f"GPA: {gpa}, Рада: {is_active_in_student_council},"
    f" Волонтерство: {has_volunteer_experience} -> Тип стипендії:"
    f" {scholarship_type}"
)