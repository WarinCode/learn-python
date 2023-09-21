import datetime
import random

# menu หลัก
def mainmenu():
    print("\n[เมนูหลัก]")
    print("1.ตรวจสุขภาพ")
    print("2.เล่นเกมส์")
    print("0.ออกจากโปรแกรม")
    

# menu 1 ตรวจสุขภาพ
def menu_healt() :
    # วัน loop รอรับค่าจาก Submenu
    # ถ้ายังไม่ return ก็ยังไม่ออกจาก loop (คือแสดงค่า Sub menu เดิม)
    while True :
        print("\n[ตรวจสุขภาพ]")
        print("1.BMI")
        print("2.ตรวจความดัน")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work = int(input("เลือก : "))
        if work == 9 :
            return 9
        elif work == 0 :
            return 0
        elif work == 1 :
            bmi()
        elif work == 2 :
            bp()
        else:
            pass

# menu 2 เล่นเกมส์
def menu_game() :
    while True :
        print("\n[เล่นเกมส]")
        print("1.เดาตัวเลข")
        print("2.ไพ่89")
        print("3.มากกว่าน้อยกว่า")
        print("9.กลับเมนูหลัก")
        print("0.ออกจากโปรแกรม")
        work = int(input("เลือก : "))
        if work == 9 :
            return 9
        elif work == 0 :
            return 0
        elif work == 1 :
            guess()
        elif work == 2 :
            card89()
        elif work == 3 :
            moreorless()
        else:
            pass

def card89() :
    print("\n[ไพ่89]")
    card1 = random.randint(1,13)
    card2 = random.randint(1,13)
    if card1 >=10 :
        point1=10
    else :
        point1=card1

    if card2 >=10 :
        point2=10
    else :
        point2=card2

    print(f"Card1 : {card1}")
    print(f"Card2 : {card2}")
    thepoint = ((point1+point2)%10)

    if thepoint == 9 :
        print ("-->P9!! ")
    elif thepoint == 8 :
        print ("-->P8!")
    elif thepoint >= 4 :
        print (f"-->Your point is :{thepoint}")
    else :
        print (f"The point is :{thepoint} draw Card3")
        card3 = random.randint(1,13)
        print(f"Card3 : {card3}")
        if card3 >=10 :
            point3=10
        else :
            point3=card3
        thepoint = ((point1+point2+point3)%10)
        print (f"+++Your point is :{thepoint}")

def moreorless() :
    the_num = random.randint(1,10)
    turn=1
    while turn<=5 :
        print (f"#{turn}:The number ->{the_num}")
        ans = input(f"Next number More (m) or Less(l) than {the_num} :")
        next_num = random.randint(1,10)
        print(f"==>> {next_num}\n")
        if (next_num > the_num and ans != 'm') or (next_num < the_num and ans != 'l') :
            break
        the_num = next_num
        turn+=1

    print(f"Game is end,You use {turn} turn ")
    if turn < 5 :
        print("You Lose!!")
    else :
        print("You Win!!")
        
def guess():
    ran_num = random.randint(1,10)
    turn = 0
    ans_num=0
    while ans_num != ran_num :
        turn+=1
        ans_num=int(input("Answer :"))
        if ans_num > ran_num:
            print(f"Less than {ans_num}")
        elif ans_num < ran_num:
            print(f"More than {ans_num}")
        elif ans_num == ran_num:
            print(f"Correct Answer is ->{ran_num}")
    print(f"**You take {turn} round")

def bmi() :
    print("[BMI]")
    wi = float(input("น้ำหนัก (kg) :")) 
    hi = float(input("ส่วนสูง (cm) :"))
    thebmi=round(wi/(hi/100)**2,2)
    if thebmi >=30 :
        thestate="อ้วนระดับ2"
    elif thebmi >=25 :
        thestate="อ้วนระดับ1"
    elif thebmi >=23 :
        thestate="น้ำหนักเกิน"
    elif thebmi >=18.5 :
        thestate="สมส่วน"
    elif thebmi < 18.5 :
        thestate="ต่ำกว่าเกณฑ์"
    print (f"+++ค่า BMI={thebmi} สถานะ{thestate}")

def bp() :
    print("[ตรวจความดัน]")
    top_p = float(input("ความดันตัวบน :"))
    bottom_p = float(input("ความดันตัวล่าง :"))

    if top_p>=180 or bottom_p >=110 :
        bp_state = "ความดันสูงมาก"    
    elif top_p>=160 or bottom_p >=100 :
        bp_state = "ความดันสูงปานกลาง"
    elif top_p>=140 or bottom_p >=90 :
        bp_state = "ความดันสูงเล็กน้อย"
    else :
        bp_state = "ความดันปกติ"
    print (f"+++{bp_state}")

def greet (name) :
    thistime=datetime.datetime.now().hour
    if(thistime<=12) :
        thegreet="ตอนเช้า"
    else :
        thegreet="ตอนบ่าย"
    print (f"สวัสดี{thegreet} คุณ{name}\n")

def farewell(name) :
    print(f"\n++ ลาก่อนคุณ{name}")
    print("ขอบคุณที่ใช้บริการ")
    print("--------------")



# main program
myname= input("ชื่อ:")
greet(myname)

# วนLoop รอรับการเลือก Menu ทำงาน
while True :
    # แสดง mainmenu
    mainmenu()
    work=int(input("เลือกหัวข้อเพื่อทำงาน : "))
    # ถ้าเลือก 0 กล่าวคำอำลา และออกจาก Loop (คือจบโปรแกรม)
    if work == 0 :
        farewell(myname)
        break
    # ถ้าเลือก 1 เรียก function ไปเมนูทำงานสุขภาพ 
    # ถ้ามีการ return เป็น0 ก็ออกจากโปรแกรม 
    elif work==1:
        if menu_healt() == 0:
            farewell(myname)
            break
    # ถ้าเลือก 2 เรียก function ไปเมนูทำงานเกมส์ 
    # ถ้ามีการ return เป็น0 ก็ออกจากโปรแกรม 
    elif work==2:
        if menu_game() == 0:
            farewell(myname)
            break
    # ถ้าตอบตัวเลขอื่นก็ผ่านให้วน Loopต่อไป
    else :
        pass