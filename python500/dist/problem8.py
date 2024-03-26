# %% [markdown]
# <h1 style="text-align: center;">บทที่ 8 IF-ELSE(PROBLEM)</h1>
# <hr>

# %%
# ข้อ 1
n = int(input("ใส่ตัวเลข >> "))
print(f"{n} เป็นเลขคู่" if n % 2 == 0 else f"{n} เป็นเลขคี่")

# %%
# ข้อ 2
n = int(input("ใส่ตัวเลข >> "))
print(n)
print("มากกว่า 0" if n > 0 else "น้อยกว่า 0")

# %%
# ข้อ 3
n = int(input("ตัวเลข >> "))
print(f"ตัวเลขที่รับมาคือ {n}")
if n > 0:
    print("positive")
elif n < 0:
    print("negative")
else:
    print("zero")

# %%
# ข้อ 4
n = int(input("ตัวเลข >> "))
print(f"ตัวเลขที่รับมาคือ {n}")
if n > 0:
    if n % 2 == 0:
        print("positive even")
    elif n % 2 != 0:
        print("positive odd")
elif n < 0:
    if n % 2 == 0:
        print("negative even")
    elif n % 2 != 0:
        print("negative odd")
elif n == 0:
    print("zero")

# %%
# ข้อ 5
width = int(input("ความกว้าง >> ")) 
length = int(input("ความยาว >> "))

def alert():
    print("กรุณากรอกจำนวนเต็มบวก")
    
if width == 0 or length == 0:
    alert()
elif width < 0 or length < 0:
    alert()
else:
    area = width * length
    print(f"พื้นที่สี่เหลี่ยมคือ {area}")

# %%
# ข้อ ุ6
year = int(input("ปี ค.ศ >> "))

print(year)
if year > 0:
    print(year + 543)
elif year <= 0:
    print("กรุณากรอกข้อมูลที่มากกว่าหรือเท่ากับ 0")

# %%
# ข้อ 7
tf = eval(input("อุณหภูมิในหน่วยฟาเรนไฮต์ >> "))
tc = None

print(f'อุณหภูมิ {tf:.2f}°f')
if tf >= 32:
    tc = (5 * (tf - 32)) / 9
    print(f'อุณหภูมิ {tc:.2f}°c')
elif tf < 32:
    print("COLD")    

# %%
# ข้อ 8
USD = eval(input("เงินดอลล่า >> "))
THB = 0

if USD > 0:
    THB = USD * 32.5
    print(f"{USD} ดอลล่า = {THB} บาท")
elif USD <= 0:
    print("you don't have money")

# %%
# ข้อ 9
THB = eval(input("เงินบาท >> "))
USD = 0
bank = 0

if THB > 0:
    USD = THB / 32.80
    bank = USD * 0.3
    print(f"เงินไทย {THB} บาท  = เงินดอลล่า {USD:.2f} ดอลล่า \nธนาคารได้กำไร {bank:.2f} ดอลล่า")
elif THB <= 0:
    print("you don't have money")

# %%
# ข้อ 10
n1 = eval(input("ตัวเลขตัวที่ 1 >> "))
n2 = eval(input("ตัวเลขตัวที่ 2 >> "))

print(f"{n1} หรือ {n2} อันไหนมากกว่ากัน")
if n1 > n2:
    print(n1)
elif n2 > n1:
    print(n2)
elif n1 == n2:
    print('มีค่าเท่ากัน')

# %%
# ข้อ 11
str1 = len(input("ข้อความที่ 1 >> "))
str2 = len(input("ข้อความที่ 2 >> "))

print(f"ความยาวของข้อความตัวที่ 1 = {str1}\nความยาวของข้อความตัวที่ 2 = {str2}")
print("same" if str1 == str2 else "not same")

# %%
# ข้อ 12
int1 = int(input("ตัวเลขจำนวนเต็ม >> "))
print(f"{int1} หารด้วย 3 ลงตัว" if int1 % 3 == 0 else f"{int1} หารด้วย 3 ไม่ลงตัว" )

# %%
# ข้อ 13
int1 = int(input("ตัวเลขจำนวนเต็ม >> "))
print(f"{int1} หารด้วย 3 และ 5 ลงตัว" if (int1 % 3 == 0) and (int1 % 5 == 0) else f"{int1} หารด้วย 3 และ 5 ไม่ลงตัว" )

# %%
# ข้อ 14
# โจทย์เดียวกับ ข้อ 13 ไม่ทำ

# %%
# ข้อ 15
a = int(input('ตัวเลขที่ 1 >> '))
b = int(input('ตัวเลขที่ 2 >> '))
c = int(input('ตัวเลขที่ 3 >> '))

if (a + b) > c:
    print('a + b > c')

# %%
# ข้อ 16
from math import *
hour = int(input("ชั่วโมง >> ")) 
minute = int(input("นาที >> ")) 
parking_fee = 0

if minute % 60 != 0:
    hour += (minute // 60) + 1;
else: hour += int(minute / 60)
for i in range(1 , hour + 1):
    if i == 1: continue
    parking_fee += 30
print(f'คุณจอดรถ {hour - 1} ชั่วโมง {minute} นาที เสียค่าจอดรถ {parking_fee:,} บาท') 

# %%
# ข้อ 17
hour = int(input("ชั่วโมง >> "))
minute = int(input("นาที >> ")) 
parking_fee = 0

if hour < 0 or minute < 0:
    print('โปรดใส่ข้อมูลที่ไม่ติดลบ')
else:
    if minute % 60 != 0:
        hour += ceil(minute / 60)
    else: 
        hour += int(minute / 60)
    for i in range(1 , hour + 1):
        if i == 1: continue
        parking_fee += 30
    print(f'คุณจอดรถ {hour if minute == 0 else hour - 1} ชั่วโมง ', end='') 
    print('' if minute == 0 else f'{minute} นาที' , end='')
    print('คุณไม่เสียค่าจอดรถ'if parking_fee == 0 else f' เสียค่าจอดรถ {parking_fee} บาท')

# %%
# ข้อ 18
from math import *

bill = int(input("บิล >> "))
hour = int(input("ชั่วโมง >> "))
minute = int(input("นาที >> ")) 
parking_fee = 0

if minute % 60 != 0:
    hour += ceil(minute / 60)
else: 
    hour += int(minute / 60)
if bill >= 1000: hour = hour - 4
elif bill < 1000: hour = hour - 1

if hour <= 0: print("คุณไม่เสียค่าจอดรถ")
else:
    for i in range(1 , hour + 1): 
        parking_fee += 30
    print('คุณเสียค่าจอดรถ' , parking_fee , 'บาท')

# %%
# ข้อ 19
bill = eval(input("เงิน >> "))
print('เงิน %s บาท' %(bill))
if bill >= 50000: bill = bill * ((100 - 20) / 100)
elif bill >= 10000: bill = bill * ((100 - 15) / 100)
elif bill >= 1000: bill = bill * ((100 - 10) / 100)
print('เงินที่ต้องจ่ายคือ %g %s' %(bill, 'บาท'))

# %%
# ข้อ 20
try:
    gender = input("เพศ >> ")
    weight = float(input("น้ำหนก >> "))
    height = int(input("ความสูง >> ")) 
except ValueError:
    print("Error! โปรดใส่ข้อมูลใหม่อีกครั้ง")
finally: 
    if gender == 'ชาย':
        print("คุณออกกำลังกาย") if weight > (height - 100) else print("คุณผู้ชายหุ่นดีเยี่ยม")
    elif gender == 'หญิง':
        print("ควรออกกำลังกาย") if weight > (height - 110) else print("คุณผู้หญิงหุ่นดี")
    else: print("Error! โปรดตอบเพศเป็น (\"ชาย\" หรือ \"หญิง\") เท่านั้น")

# %%
# ข้อ 21
velocity = float(input("อัตราเร็วรถยนต์ >> "))
if velocity > 120: print("ออกใบสั่ง")

# %%
# ข้อ 23
listen_time = eval(input("จำนวนชั่วโมงที่ฟังเพลง >> "))
print("อันตรายต่อหู") if listen_time > 4 else print("ขอให้มีความสุขกับการฟังเพลง")

# %%
# ข้อ 24
status = input("สถานะการเดินทาง >> ")
distance = float(input("ระยะทาง >> "))
bill = 0

if status == 'คล่องตัว':
    bill = distance * 10
elif status == 'ปานกลาง':
    bill = distance * 12
elif status == 'หนาแน่น':
    bill = distance * 15
print(f'ค่าโดยสารของคุณคือ {bill} บาท')

# %%
# ข้อ 25
score = int(input('คะแนน >> '))
print("Pass" if score >= 50 else "Fail")

# %%
# ข้อ 26
score = int(input("คะแนนสอบนักเรียน >> "))
if score >= 80: print('A')
elif 80 >= score >= 70: print('B')
elif 70 >= score >= 60: print('C')
elif 60 >= score >= 50: print('D')
else: print('F')

# %%
# ข้อ 27
isMember = input('คุณเป็นสมาชิกของรานค้าหรือไม่ (yes / no) >> ')
bill = float(input('บิล >> '))

if isMember == 'yes':
    if bill >= 5000: print('คุณได้ส่วนลด 15%')
    elif bill >= 1000: print('คุณได้ส่วนลด 10%')
    elif bill >= 500: print('คุณได้ส่วนลด 5%')
elif isMember == 'no': print('คุณไม่ได้รับส่วนลด')

# %%
# ข้อ 28
current = input("เลือกสกุลเงินที่ต้องการแลกเปลี่ยน >> ")
amount = float(input("จำนวนเงิน >> "))
THB = 0

if current == 'USD':
    THB = amount * 32.5 
elif current == 'JPY':
    THB = amount * 0.29
print(THB , 'บาท')   

# %%
# ข้อ 29
order = input('สั่งอาหาร >> ')
amount = int(input("จำนวนเงิน >> "))
menu = ('ไข่ดาว' , 'ไข่เจียว' , 'ไข่ต้ม')
if order == menu[0]: amount *= 7
elif order == menu[1]: amount *= 10
elif order == menu[2]: amount *= 5
print('ร้านเรามี ',*menu)
print(f'{amount} บาท')

# %%
# ข้อ 30
order = input('สั่งอาหาร >> ')
menu = ('ไข่ดาว' , 'ไข่เจียว' , 'ไข่ต้ม')
if order == menu[0]: print('แนะนำให้สั่งคู่กับต้มจืดไข่น้ำ')
elif order == menu[1]: print('แนะนำให้สั่งคู่กับไข่ลูกเคย')
elif order == menu[2]: print('แนะนำให้สั่งคู่กับยำไข่ดาว')


