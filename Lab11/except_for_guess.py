import random

print("\n[เดาตัวเลข]")
ran_num = random.randint(1,10)
ans_num = 0
_round = 1
#print(ran_num)
#ให้ดักจับและเตือนใส่ข้อมูลเป็นตัวเลข
while ans_num != ran_num :
    try:
        ans_num=int(input(f"[{_round}]Answer is :"))
        if ran_num > ans_num :
            print (f"++มากกว่า {ans_num}")
        elif ran_num < ans_num :
            print (f"--น้อยกว่า {ans_num}")
        else :
            print ("ถูกต้อง!!!")
            break
        _round+=1
    except ValueError as err:
        print(err)
        print('ต้องใส่เป็นตัวเลขจำนวนเต็มเท่านั้นเท่านั้น!')
print (f"*** You take {_round} rounds ***")