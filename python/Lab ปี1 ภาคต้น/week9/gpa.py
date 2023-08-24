# ข้อ 1
subjects = ('DataCom' , 'OS' , 'ComArch')
grade  , gpa = [] , []

for s in subjects:
    gpa.append(int(input(f'หน่วยกิตของวิชา {s} : ')))
    grade.append(int(input(f'เกรดของวิชา {s} : ')))     
print(f'ลงทะเบียนทั้งหมด = {sum(gpa)} หน่วย\nGPA = {sum(grade) / grade.__len__()}')