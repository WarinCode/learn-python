subject = {    "01":{ "programming":3},
               "02":{ "digital":3},
               "03":{ "physic":3},
                "04":{"calculus":3}
        }

def get_name():
    thename=input("Student Name :")
    return thename

def enroll (theset,scredit):
    inpcode=input("Enroll :")
    if inpcode in subject :
        enrsubj=dict()
        enrsubj=subject[inpcode]
        for subj,credit in enrsubj.items() :
            theset.add(subj)
            scredit=scredit+credit
            print(f"--> {inpcode}:{subj}:{credit}units OK!!")
        wk=1
    elif inpcode=='end' :
        wk=0
    else:
        print (f"--Notfound SUbject CODE: '{inpcode}'")
        wk=1
    return theset,scredit,wk

def show_enroll():
    j=0
    for subj in enroll_set :
        j+=1
        print(j,'.',subj)


enroll_set = set()
stu_name = get_name()

sum_credit = 0
work=1
while work!=0 :
    enroll_set,sum_credit,work = enroll (enroll_set,sum_credit)

print (f"{stu_name} enroll {len(enroll_set)}subj ,{sum_credit}units")
show_enroll()
