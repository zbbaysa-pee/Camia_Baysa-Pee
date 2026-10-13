# Ziva Zenith Victorious Baysa-Pee
# 8-Camia

score_one = 0
score_two = 0
score_three = 0
average = 0

def display_header():
 print("STUDENT PERFORMANCE EVALUATOR")
 print("-----------------------------")

# Define a function to get the name and assessment scores of the student
def get_student_info(name, score_one, score_two, score_three):
    name = str(input("Enter student name: "))
    score_one = int(input("Enter Assessment 1: "))
    score_two = int(input("Enter Assessment 2: "))
    score_three = int(input("Enter Assessment 3: "))

    return name, score_one, score_two, score_three
# Define a function to calculate the average of the scores and determine the performance level
def evaluate_performance(average, performance_level):
    average = (score_one + score_two + score_three) / 3

    if average >= 90:
        performance_level = "Outstanding"
    elif average >= 85:
        performance_level = "Very Satisfactory"
    elif average >= 80:
        performance_level = "Satisfactory"
    elif average >= 75:
        performance_level = "Fairly Satisfactory"
    else:
        performance_level = "Needs Improvement"
    return average, performance_level

def display_report('name', 'average', 'score_one', 'score_two', 'score_three', 'performance_level'):
    print("STUDENT PERFORMANCE REPORT")
    print(f"Student Name: {name}")
    print(f"Assessment Scores: {"score_one", "score_two", "score_three"}")
    print(f"Average Score: {average}")
    print(f"Performance Level: {performance_level}")
report_heading = "STUDENT PERFORMANCE EVALUATOR"

display_header()
get_student_info()
evaluate_performance()
print(report_heading)
display_report()

# Two Local Variables: average and performance_level
# One Global Variable: report_heading