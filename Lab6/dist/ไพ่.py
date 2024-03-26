# ข้อ 3
from random import *

point = 0
card = {
    1:randint(1,13),
    2:randint(1,13),
}
value = {
    1: None,
    2: None
}

def randomCard():
    global point
    for i in card:
        value[i] = 10 if card[i] >= 10 else card[i]
        point += value[i]
    point %= 10

randomCard()
print(f'ได้ไพ่ : {card[1]} : {card[2]} = {point} แต้ม')

if point < 4:
    print('แต่มต่ำต้องเรียกไพ่ใบที่ 3')    
    card[3] = randint(1,13)
    value[3] = 0
    randomCard()
    print(f'ได้ไพ่ : {card[1]} : {card[2]} : {card[3]} = {point} แต้ม')

    
# card1 = randint(1,13)
# card2 = randint(1,13)
# p1 = p2 = 0

# p1 = 10 if card1 >= 10 else card1
# p2 = 10 if card1 >= 10 else card2
# point = (p1 + p2) % 10
# print(f'ได้ไพ่ : {card1} : {card2} = {point} แต้ม')

# if point < 4:
#     print('แต่มต่ำต้องเรียกไพ่ใบที่ 3')
#     card3 = randint(1,13)
#     p3 = 10 if card3 > 10 else card3
#     point = (p1 + p2 + p3) % 10
#     print(f'ได้ไพ่ : {card1} : {card2} : {card3} = {point} แต้ม')