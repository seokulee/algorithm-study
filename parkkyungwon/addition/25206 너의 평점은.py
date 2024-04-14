score_to_int = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 
                'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0,
                'F': 0.0}

scores = []
grades = []
for _ in range(20):
    temp = input().split()
    grade, score = float(temp[1]), temp[2]

    if score == 'P':
        continue

    scores.append(grade * score_to_int[score])
    grades.append(grade)

print(sum(scores) / sum(grades))