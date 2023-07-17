#include <stdio.h>
#include <math.h>

// ข้อ 2
void main()
{
    float Weight, Height;

    puts("How many kilograms do you weigh ?");
    scanf("%g", &Weight);
    puts("How many meters are you tall?");
    scanf("%g", &Height);

    const float BMI = (float)Weight / pow(Height, 2);
    printf("Your BMI value: %g\n", BMI);
    if (BMI < 18.5)
    {
        printf("You are skinny.");
    }
    else if (BMI >= 18.5 && BMI <= 22.90)
    {
        printf("You are normal weight.");
    }
    else if (BMI >= 23 && BMI <= 24.90)
    {
        printf("You are chubby.");
    }
    else if (BMI > 24.90)
    {
        printf("You are too fat.");
    }
}