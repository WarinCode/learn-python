from random import randint

n1 = randint(1,10)
turn = 0
while turn < 5:
    turn += 1
    print(f'#{turn}:The number -> {n1}')
    guess = input(f'Next number More(m) or Less(l) than {n1} : ')
    n2 = randint(1,10)  
    print(n2)
    if guess == 'l':
        if n2 > n1: 
            n1 = n2
            continue
        else: break
    elif guess == 'm':
        if n2 < n1: 
            n1 = n2
            continue
        else: break
print(f'Game is end, You use {turn} turn')
print('You Loss!!' if turn < 5 else 'You Win!!')