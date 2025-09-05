#include <stdio.h>
#include <math.h>

int main(){
    int UserNum;

    printf("Enter a Number :  ");
    scanf("%d", &UserNum);
    printf("The sum of counting Numbers up to %d is %d", UserNum, (UserNum+1)*UserNum/2);

    return 0;
}