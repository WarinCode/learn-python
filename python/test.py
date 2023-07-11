# %%
# ทดสอบ
print("Hello World!" , 'Hello Jupyter Notebook!' , sep='\n')

# %%
# ตัวอย่างที่ 1
import datetime
date = datetime.datetime.now()
year = date.strftime("%Y")
birthday = int(input('คุณเกิดปี พ.ศ >>> '))
age = abs(int(birthday - 543) - int(year))
print(F'อายุของคุณคือ {age} ปี')

# %%
# ตัวอย่างที่ 2
price  = eval(input('ราคาสินค้า >>> '))
quantity  = int(input('จำนวนสินค้า >>> '))
total = price * quantity
print(f'ราคาสินค้าทั้งหมด {total:,.2f} บาท')

# %%
# ตัวอย่างที่ 3
n = int(input('สูตรคูณแม่ >> '))
l = int(input('ความยาว >> '))

def multiplication_table(number = n , lenght = l):
    print(f'สูตรคูณแม่ {number}')
    for i in range(0,lenght):
        i += 1
        print(f'{number} x {i} = {number  * i}')

multiplication_table()

# %%
# ตัวอย่างที่ 4
formula = 'n! = n * (n-1) * (n-2) * .... * 1'
number = abs(int(input('ตัวเลข >> ')))

def factorial(n):
    sum = 1
    if(n == 0): 
        sum
    else:
        while(n > 1):
            sum *= n
            n -= 1 
    return sum
    
print(f'''{formula}
{number}! มีค่าเท่ากับ {format(factorial(number) , ',')}
    ''' )

# %%
# ตัวอย่างที่ 5
from math import *
x = eval(input('ตัวเลขที่จะยกกำลัง >> '))
y = eval(input('ยกกำลังเท่าไหร่ >> '))

def exponent(x , y):
    return pow(x , y)

print(f'{x} ยกกำลัง {y} = {exponent(x,y)}')

# %%
# ตัวอย่างที่ 6
Speed = eval(input('ระยะทาง >> '))
Time = eval(input('เวลา >> '))
def Velocity(s , t):
    v = s / t
    print(f'อัตราเร็วคือ {v:,.2f} m/s')

Velocity(Speed , Time)

# %%
# ตัวอย่างที่ 7
from math import *

choose = int(input('เลือกสูตรที่ >> '))
print(f'''
    1.) v = u + at
    2.) s = (u + v /2)t 
    3.) s = ut + 1/2 at2
    4.) s = vt - 1/2 at2
    5.) v2 = u2 + 2as
    
    => เลือกสูตรที่ {choose}
''')

def straight_motion():
    if choose == 1:
        a = eval(input('ความเร่ง >> '))
        t = eval(input('เวลา >> '))
        u = eval(input('ความเร็วต้น >> '))
        v = u + (a * t)
        return f'ความเร็วเท่ากับ {v:,.2f} m/s'
    elif choose == 2:
        t = eval(input('เวลา >> '))
        u = eval(input('ความเร็วต้น >> '))
        s = ((u + t) / 2) * t
        return f'ระยะทางเท่ากับ {s:,.2f} m'
    elif choose == 3:
        a = eval(input('ความเร่ง >> '))
        t = eval(input('เวลา >> '))
        u = eval(input('ความเร็วต้น >> '))
        s = (u * t) + (1 / 2 * (a * (pow(t , 2))))
        return f'ระยะทางเท่ากับ {s:,.2f} m'
    elif choose == 4:
        a = eval(input('ความเร่ง >> '))
        t = eval(input('เวลา >> '))
        u = eval(input('ความเร็วต้น >> '))
        s = (u * t) - (1 / 2 * (a * (pow(t , 2))))
        return f'ระยะทางเท่ากับ {s:,.2f} m'
    elif choose == 5:
        a = eval(input('ความเร่ง >> '))
        s = eval(input('ระยะทาง >> ')) 
        u = eval(input('ความเร็วต้น >> '))
        v2 = pow(u , 2) + (2 * (a * s))
        return f'ความเร็วเท่ากับ {v2:,.2f} m/s'

if 6 > choose:
    print(straight_motion())
else: 
    print('โปรดเลือกตัวเลขตั้งแต่ 1 ถึง 5 เท่านั้น!')

# %%
# ตัวอย่างที่ 8
import math as m 

f = '''
    สูตรการหาพื้นที่ของรูปเรขาคณิตต่างๆ
 
1. สูตรการหาพื้นที่สี่เหลี่ยมจัตุรัส = ด้าน x ด้าน หรือ 1/2 x ผลคูณของเส้นทแยงมุม
2. สูตรการหาพื้นที่สี่เหลี่ยมผืนผ้า = กว้าง x ยาว
3. สูตรการหาพื้นที่สามเหลี่ยม = 1/2 x ฐาน x สูง
4. สูตรการหาพื้นที่สี่เหลี่ยมขนมเปียกปูน = ฐาน x สูง หรือ 1/2 x ผลคูณของเส้นทแยงมุม
5. สูตรการหาพื้นที่สี่เหลี่ยมด้านขนาน = ฐาน x สูง
6. สูตรการหาพื้นที่สี่เหลี่ยมรูปว่าว = 1/2 x ผลคูณของเส้นทแยงมุม
7. สูตรการหาพื้นที่สี่เหลี่ยมด้านไม่เท่า = 1/2 x เส้นทแยงมุม x ผลบวกของเส้นกิ่ง
8. สูตรการหาพื้นที่วงกลม = พาย x รัศมี2
''' 
print(f)
c = int(input('เลือกตัวเลข >> '))
print(f'คุณเลือกสูตรที่ {c}')

def Geometric_formula():
    if c == 1:
        side = int(input('ด้าน >> '))
        quadrature = m.pow(side , 2)
        print(f'พื้นที่สี่เหลี่ยมจัตุรัสคือ {quadrature}')
    elif c == 2:
        wide = int(input('กว้าง >> '))
        long = int(input('ยาว >> '))
        rectangle = wide * long
        print(f'พื้นที่สี่เหลี่ยมผืนผ้าคือ {rectangle}')
    elif c == 3:
        base = int(input('ฐาน >> '))
        high = int(input('สูง >> '))
        triangle = 1 / 2 * (base * high)
        print(f'พื้นที่สามเหลี่ยมคือ {triangle}')
    elif c == 4:
        if 1:
            base = int(input('ฐาน >> '))
            high = int(input('สูง >> '))
            rhombus1 = base * high
            print(f'พื้นที่สี่เหลี่ยมขนมเปียกปูนคือ {rhombus1}')
        else:
            product_of_diagonal = base * high
            rhombus2 = 1 / 2  * product_of_diagonal
            print(f'พื้นที่สี่เหลี่ยมขนมเปียกปูนคือ {rhombus2}')

Geometric_formula()

# %%
# ตัวอย่างที่ 9
import random as r
lenght = int(input('ความยาวของรหัสผ่าน >> '))

def password_generator(l):
    global password
    num = '0123456789'
    char = 'abcdefghijklmnopqrstuvwxyz'
    sym = '+-*/%$#@<>=|?!^_.,(){}[];:'
    total = num + char + char.upper() + sym
    if (l > 0  and l <= 17 and type(l) == type(0)):
        try:
            list = []
            password = ''
            i = 0; int(i)
            for i in range(0,l+1,1):
                ran = r.choice(total)
                list.append(ran)
                password += '' + list[i]
        except:
            pass
        finally:
            return f'password >> {password}'
    elif (0 <= l >= 17): 
        return f'ไม่สามารถสร้างรหัส่านที่มีความยาว {l}'

print(password_generator(lenght))

# %%
# ตัวอย่างที่ 10
n = int(input('ตัวเลข >> '))
print(f'เลข {n}')

if n % 2 == 0:
    print('เป็นเลขคู่')
elif n % 2 != 0:
    print('เป็นเลขคี่')

# %%
# ตัวอย่างที่ 11
li = []
def inputData(l):
    for i in range(0, l ,1):
        li.append(int(input(f'รับข้อมูลจำนวนที่ {i + 1}')))
        
    print(f'ข้อมูลทั้งหมด => {li}')
    print(f'ผลรวมทั้งหมดเท่ากับ {sum(li)}')
    print(f'ค่าเฉลี่ยเลขคณิตเท่ากับ {sum(li) / li.__len__():,.2f}')
    
inputData(int(input('รับตัวเลขกี่ตัว?')))

# %%
# ตัวอย่างที่ 12
l = [*range(1 , 10 + 1)]
n = eval(input('โปรดส่งตัวเลขมา ค้นหาข้อตัวเลขว่าเป็นเลข 1 ถึง 10 ไหม'))

if n in l: print(f'{n} อยู่ในช่วงตัวเลข 1 ถึง 10')
else: print(f'{n} ไม่อยู่ในช่วงตัวเลข 1 ถึง 10')


