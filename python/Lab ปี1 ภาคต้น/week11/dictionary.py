subject = []
i = 0
while True:
    i += 1
    s = input(f'วิชา_{i} : ')
    if s == 'end': 
        i = 0
        break
    else: subject.append(s)
print(f'มีทั้งหมด {subject.__len__()} วิชา =',subject)
dic = {}
for i in subject:
    dic[i] = int(input(f'คะแนนวิชา {i}: '))
print(dic)
while True:
    key = input("หาข้อมูลวิชา : ")
    if key in dic: print(f"วิชา {key} = {dic[key]}")
    elif key == 'end': break
    elif key not in dic: print(f'หาวิชา {key} ไม่พบ')