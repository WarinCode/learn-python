#include <stdio.h>
#include <stdbool.h>

void main(){
    // Exercise 1
    // กำหนดให้
    short a = 10, b = 20, c = 30;
    /* 0 เทียบเท่า false , 1 เทียบเท่า true */

    printf("%d\n", (a != b) && (b == c));
    // output: 0 
    printf("%d\n", (a < b) || (b >= c));
    // output: 1
    printf("%d\n", a <= b);
    // output: 1
    printf("%d\n", !(a <= b));
    // output: 0 
    printf("%d", !(a <= 5) && (c != 20));
    // output: 1

    // Exercise 2
    // ไม่ได้กำหนดค่าข้อมูลมาให้ ตัวแปรบอกแค่ชนิดข้อมูลอย่างเดียว
    float Amount;
    bool Member; // true เป็นสมาชิก , false ไม่เป็นสมาชิก 

    bool b1 = Amount > 10000;
    bool b2 = Member == false && Amount == 0;
    bool b3 = Amount >= 1;
    bool b4 = Amount <= 20000 && Member == true;
    bool b5 = Amount < 10000 || Member == false;
    bool b6 = Amount > 50000 || Amount < 10000;
    bool b7 = Amount >= 20000 && Amount <= 30000; 
}