# ข้อ 2
Height = float(input("คุณสูงกี่เมตร ? "))
Weight = float(input("คุณหนักกี่กิโลกรัม ? "))
BMI = Weight / pow(Height , 2)

print("Your BMI value:" ,  format(BMI , '.2f'));

if BMI < 18.5:
    print("You are skinny.")
elif 18.5 <= BMI <= 22.90:
    print("You are normal weight.")
elif 23 <= BMI <= 24.90:
    print("You are chubby.")
elif BMI > 24.90:
    print("You are too fat.")