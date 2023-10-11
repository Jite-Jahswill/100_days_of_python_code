# Coding challenge 1

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Dont change the code above
students_grades = {}

def grades_to_scores(scores):
    if scores >= 91:
        students_grades["grades"] = "Outstanding"
    elif scores >= 81 and scores <= 90:
        students_grades["grades"] = "Exceeds Expectations"
    elif scores >= 71 and scores <= 80:
        students_grades["grades"] = "Acceptable"
    elif scores <= 70:
        students_grades["grades"] = "Fail"
        
for student in students_grades:
    scores = student_scores[student]
    
    
grades_to_scores(scores=scores)  
    
    # or
for student in students_grades:
    scores = student_scores[student]
    if scores >= 91:
        students_grades[student] = "Outstanding"
    elif scores >= 81 and scores <= 90:
        students_grades[student] = "Exceeds Expectations"
    elif scores >= 71 and scores <= 80:
        students_grades[student] = "Acceptable"
    elif scores <= 70:
        students_grades[student] = "Fail"
        
        
# dont touch the code below
print(students_grades)

# Coding challenge 3

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12},
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 31},
]
# DO NOT Change the code above

# TODO: Write the function that will allow new country to be added to the travel_log.
def add_new_country(country, number_of_visit, cites_seen):
     new_country = {}
     new_country["country"] = country
     new_country["visits"] = number_of_visit
     new_country["cities"] = cites_seen
     travel_log.append(new_country)


# DO NOT Change the code below
add_new_country(country="Russia", number_of_visit=2, cites_seen=["Moscow", "Saint Petersburg"])
print(travel_log)