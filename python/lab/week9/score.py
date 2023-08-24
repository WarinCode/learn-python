# ข้อ 2
subjects = ('DataCom' , 'OS' , 'ComArch')
score = []

for i in subjects:
    for j in range(3):
        s = eval(input(f'คะแนนสอบครั้งที่ {j + 1} {subjects[j]} : '))
        score.append(s)
    print(f'ผลรวมคะแนนของวิชา {i} = {sum(score)}\n')
    score.clear()