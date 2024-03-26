#include <stdio.h>

// ข้อ 1
float discount(float price , int percent){
    const float formulaOfProductDiscount = price * ((100 - percent)  / (float)100);
    return formulaOfProductDiscount;
}

void main(){
    float Amount , Discount;
    char Membership;

    puts("Amount of a product total price ?");
    scanf("%g" , &Amount);
    getchar();
    puts("Are you a membership ?");
    scanf("%c", &Membership);

    if(Amount > 5000 && Membership == 'Y' || Membership == 'y'){
        Discount = discount(Amount , 20);
    } else if(Amount > 5000 && Membership == 'N' || Membership == 'n'){
        Discount = discount(Amount , 10);
    } else {
        Discount = discount(Amount , 5);
    }

    printf("You pay the price %g bath" , Discount);
}