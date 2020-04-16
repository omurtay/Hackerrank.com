student= []

for i in range(int(input())):
    name = input()
    score = float(input())
    student.append([name, score])

scores = sorted({s[1] for s in student})
names = sorted(s[0] for s in student if s[1] == scores[1])

print('\n'.join(names))