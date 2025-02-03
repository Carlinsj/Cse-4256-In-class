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

#Question 5
def course_average(di):
    averages = {}
    
    for student, scores in di.items():
        midterm1, midterm2, final = scores
        weighted_avg = (0.3 * midterm1) + (0.3 * midterm2) + (0.4 * final)
        averages[student] = round(weighted_avg) 
    return averages

#Question 6
def list_to_dict(li):
    frequency_dict = {}
    
    for num in li:
        if num not in frequency_dict:
            frequency_dict[num] = 1  
        else:
            frequency_dict[num] += 1  
    return frequency_dict

#Question 7
def dict_to_list(di):
    result_list = []
    
    for key, value in di.items():
        result_list.extend([key] * value) 
    return result_list

#Question 8
def most_cats(di):
    max_cats = 0
    person_with_most_cats = ""

    for person, pets in di.items():
        num_cats = pets.get("Cats", 0)  
        if num_cats > max_cats:
            max_cats = num_cats
            person_with_most_cats = person  
    return person_with_most_cats
