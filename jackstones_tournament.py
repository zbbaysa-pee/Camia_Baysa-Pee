scores = []
exit = False
white not exit:
    valid = False
    while valid = False:
        score = int(input(f"Enter Score {i}: "))

    if 0 < score < 10:
        scores.append(score)
        valid = True
        print(f"Original Scores: {scores}")
    else:
        print("Invalid score! Enter a score from 0 to 10.")
        score = int(input("Enter score to add: "))
print(f"Updated Scores: {scores}")
backup = scores.copy()
print("Backup successfully created.")

choice = int(input("Enter your choice: "))
if choice == 1:
    print(f"Current List: {scores}")
elif choice == 2:
    while valid == False:
    add_score = int(input("Enter score to add: "))
    if 0 < add_score < 10:
        scores.append(add_score)
        print(f"Updated Scores: {scores}")
        valid = True
    else:
        print("Invalid score! Enter a score from 0 to 10.")
elif choice == 3:
    insert_score = int(input("Enter score to add: "))
    index = int(input("Enter index of score to add: "))
    if 0 < insert_score < 10:
        scores.append(index, insert_score)



