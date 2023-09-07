student = []
subject = []
i = 1
while True:
    name = input(f'ชื่อนิสิต_{i} : ')
    i += 1
    if name == 'end': 
        i = 0
        break
    else: student.append(name)
print(f'มีนิสิต {student.__len__()} คน =',student)
while True:
    i += 1
    s = input(f'วิชา_{i} : ')
    if s == 'end': break
    else: subject.append(s)
print(f'มีทั้งหมด {subject.__len__()} วิชา =',subject)
for j in range(3):
    for k in range(3):
        print(f"{student[j]} -> {subject[k]}")