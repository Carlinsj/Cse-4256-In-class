#Question 1
def grades(di):
    grade_dict = {}
    for student, score in di.items():
        if score >= 90:
            grade_dict[student] = 'A'
        elif score >= 80:
            grade_dict[student] = 'B'
        elif score >= 70:
            grade_dict[student] = 'C'
        elif score >= 60:
            grade_dict[student] = 'D'
        else:
            grade_dict[student] = 'E'
    return grade_dict

#Question 2
def letter_grades(di):
    grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0} 
    
    for grade in di.values():
        if grade in grade_count:
            grade_count[grade] += 1
    
    return grade_count

#Question 3
def letter_grades_2(di):
    grade_students = {'A': set(), 'B': set(), 'C': set(), 'D': set(), 'E': set()}  
    
    for student, grade in di.items():
        if grade in grade_students:
            grade_students[grade].add(student)
    
    return grade_students

#Question 4
def highest_scores(di):
    highest_score = 0
    top_students = set()

    for student, scores in di.items():
        max_score = max(scores)  # Find the highest quiz score for the student
        
        if max_score > highest_score:  # Update highest score and reset set
            highest_score = max_score
            top_students = {student}
        elif max_score == highest_score:  # Add student to the set if tied
            top_students.add(student)

    return top_students