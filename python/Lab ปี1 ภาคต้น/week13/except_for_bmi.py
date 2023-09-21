def bmi(wi,hi):
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
    return thebmi,thestate

#ตรวจจับและบอกให้ใส่ค่าตัวเลข
#ตรวจจับและไม่ให้ตัวหารเป็น 0 
print("[BMI]")
while True :
    try:
        weight = float(input("น้ำหนัก (kg) :")) 
        height = float(input("ส่วนสูง (cm) :"))
        print("กำหนดค่าเป็นตัวเลข")
        mybmi,mystate=bmi(weight,height)
    except ValueError as err:
        print(err)
        print('ค่าน้ำหนักและส่วนสูงต้องเป็นตัวเลขเท่านั้น!')
    except ZeroDivisionError as err:
        print(err)
        print('ค่าความสูงจะต้องไม่เป็นค่า 0')
    else:
        print (f"+++ค่า BMI={mybmi} สถานะ{mystate}")
        break