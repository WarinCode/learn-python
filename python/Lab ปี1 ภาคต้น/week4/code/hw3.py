# ข้อ 3
Top = int(input("ความดันโลหิตตัวบนคุณคือ >> "))
Low = int(input("ความดันโลหิตตัวล่างคุณคือ >> "))

if Top < 120 and Low < 80:
    print("Good blood pressure.")
elif Top < 129 and Low < 84:
    print("Normal blood pressure.")
elif Top < 139 and Low < 89:
    print("Quite high blood pressure.")
elif Top > 139 and Low > 89:
    print("High blood pressure.")