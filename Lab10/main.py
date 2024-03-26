subject = {
    "programming": 3,
    "digital": 3,
    "physic": 3,
    "calculus": 3,
    "chemical": 3,
    "biology": 3,
    "marketing": 2,
    "ethics": 2,
    "english": 2,
    "chinese": 2,
    "football": 2,
    "badminton": 2,
    "softball": 2,
}

enroll_set = set()
sum_credit = 0
work = 1
get_name = lambda: input('ชื่อนิสิต : ')
stu_name = get_name()

print(f'สวสัดีคุณ {stu_name} ระบุวิชาที่ต้องการลงทะเบียน')

def enroll(_set , credit , w = 1):
    thesubj = input('วิชา : ')
    isEnd = thesubj == 'end'
    if isEnd: w = 0
    if thesubj in subject:
        _set.add(thesubj);
        credit += subject[thesubj]
    elif thesubj not in subject and not isEnd:
        print(f"--ไม่เปิดวิชา '{thesubj}'")
    return [_set , credit , w]
        
while work != 0:
    enroll_set, sum_credit, work = enroll(_set = enroll_set, credit= sum_credit)

def show_enroll():
    print(f"\n{stu_name} ลงทะเบียน {len(enroll_set)}วิชา ,{sum_credit}หน่วย")
    for i , j in enumerate(enroll_set):
        print(f'{i + 1} . {j}')
        
show_enroll()
