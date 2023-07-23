# ข้อ 4
book= {
    1: int(input("ราคาหนังสือเล่มที่ 1 >> ")),
    2: int(input("ราคาหนังสือเล่มที่ 2 >> ")),
    3: int(input("ราคาหนังสือเล่มที่ 3 >> "))
}

_min = min(*book.values())
total = sum(list(book.values()))
print(f"ราคาหนังสือทั้ง 3 เล่ม {total} บาท")
print(f"ราคาหนังสือ 2 เล่ม {total - _min} บาท")