#include <stdio.h>

using namespace std;

int main()
{
    int e, s, m;
    int year=1;
    
    scanf("%d %d %d",&e,&s,&m); // 1~15, 1~28, 1~19
    while(1){
        if((year-e)%15==0 && (year-s)%28==0 && (year-m)%19==0){
            break;
        }
        else year++;
    }
    printf("%d\n",year);
    return 0;
}