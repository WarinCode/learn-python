# ข้อ 2
li = []
for n in range(3):
    book = eval(input(f"ราคาหนังสือเล่มที่ {n + 1} >> "))
    li.append(book)
print(f'ราคาหนังสือรวม = {sum(li)}')
print(f'ราคาหนังสือที่ต้องจ่ายจริง = {sum(li) - min(*li)}')