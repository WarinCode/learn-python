# 2.สุ่มไพ่
from random import *

def ran(l1 , l2):
    card = []
    for i in range(0 , 2):
        card.append(randint(l1 , l2))
        print(f'สุ่มไพ่รอบที่ {i + 1} = {card[i]}')
    point = f'คุณได้แต้ม {choice(card)}'
    print(point)
ran(1 , 11)