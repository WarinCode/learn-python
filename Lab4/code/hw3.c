#include <stdio.h>

// ข้อ 3
void main(){
    int Top , Low;

    puts("Your systolic blood pressure is >> ");
    scanf("%d" , &Top);
    puts("Your lower blood pressure is >> ");
    scanf("%d" , &Low);

    if(Top < 120 && Low < 80){
        printf("Good blood pressure.");
    } else if(Top < 129 && Low < 84){
        printf("Normal blood pressure.");
    } else if(Top < 139 && Low < 89){
        printf("Quite high blood pressure.");
    } else if(Top > 139 && Low > 89){
        printf("High blood pressure.");
    }
}