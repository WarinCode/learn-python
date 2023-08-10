# ข้อ 3
from random import *
card1 = randint(1,13)
card2 = randint(1,13)
p1 = p2 = 0

p1 = 10 if card1 >= 10 else card1
p2 = 10 if card1 >= 10 else card2
point = (p1 + p2) % 10
print(f'ได้ไพ่ : {card1} : {card2} = {point} แต้ม')

if point < 4:
    print('แต่มต่ำต้องเรียกไพ่ใบที่ 3')
    card3 = randint(1,13)
    p3 = 10 if card3 >= 10 else card3
    point = (p1 + p2 + p3) % 10
    print(f'ได้ไพ่ : {card1} : {card2} : {card3} = {point} แต้ม')