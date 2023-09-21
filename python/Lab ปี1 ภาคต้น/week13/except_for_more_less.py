import random
the_num = random.randint(1,10)
turn=1
#ถ้าไม่ใช่ m หรือ l ให้ raise ว่าค่าไม่ถูกต้อง และทำงานต่อได้
while turn<=5 :
    try:
        print (f"#{turn}:The number ->{the_num}")
        ans = input(f"Next number More (m) or Less(l) than {the_num} :")
        next_num = random.randint(1,10)
        print(f"==>> {next_num}\n")
        if ans != "m" and ans != 'l': 
            raise Warning('ใส่ค่าไม่ถูกต้อง!ใส่เเค่ "m" หรือ "l" เท่านั้น')
        if (next_num > the_num and ans != 'm') or (next_num < the_num and ans != 'l') :
            break
        the_num = next_num
        turn+=1
    except Warning as err:
        print(err)

print(f"Game is end,You use {turn} turn ")
if turn < 5 :
    print("You Lose!!")
else :
    print("You Win!!")