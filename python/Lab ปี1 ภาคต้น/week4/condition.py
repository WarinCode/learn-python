# Exercise 1
# กำหนดให้
a , b , c = 10 , 20 , 30

print((a != b) and (b == c)) 
# output: False
print((a < b) or (b >= c))
# output: True
print(a <= b)
# output: True
print(not(a <= b))
# output: False
print(not(a <= 5) and (c != 20))
# output: True

# # Exercise 2
# # ไม่ได้กำหนดค่าข้อมูลมาให้ ตัวแปรบอกแค่ชนิดข้อมูลอย่างเดียว
Amount = float() 
Member = bool() # True เป็นสมาชิก , False ไม่เป็นสมาชิก 

Amount > 10_000
(Member == False) and (Amount == 0)
Amount >= 1
(Amount <= 20_000) and (Member == True)
(Amount < 10_000) and (Member == False)
(Amount > 50_000) or (Amount < 10_000)
30_000 >= Amount >= 20_000  # (Amount >= 20_000) and (Amount <= 30_000