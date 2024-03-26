#include <stdio.h>

void main(){
    int book1 , book2, book3 , total , min; 

    printf("Enter your a book1 price >> ");
    scanf("%d" , &book1);
    printf("Enter your a book1 price >> ");
    scanf("%d" , &book2);
    printf("Enter your a book1 price >> ");
    scanf("%d" , &book3);

    total = book1 + book2 + book3;

    if(book1 < book2 && book1 < book3){
        min = book1;
    } else if(book2 < book1 && book2 < book3) {
        min = book2;
    } else {
        min = book3;
    }

    printf("total of price a three book: %d" , total);
    puts("");
    printf("total of price a three book: %d" , total - min);
}