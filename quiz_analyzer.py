# Activity 1 - Quiz Score Analyzer

scores = []
for i in range(1, 6):
    score = int(input(f"Enter Quiz {i}: "))
    scores.append(score)
print(f"Number of quizzes: {len(scores)}")
print(f"Total Score: {sum(scores)}")
print(f"Average Score: {sum(scores)/len(scores):.2f}")
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Ascending: {sorted(scores)}")
print(f"Descending: {sorted(scores, reverse=True)}")
print(f"Original Scores: {scores}")

