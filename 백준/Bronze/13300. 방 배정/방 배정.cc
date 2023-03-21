#include <stdio.h>
using namespace std;

int main()
{
    int n, k;
    int arry[2][6]={0}; //성별 학년 
    int sum = 0;    
    scanf("%d %d", &n,&k);
    for(int i=0; i<n; i++){
        int s,y;
        scanf("%d %d", &s,&y);
        arry[s][y-1]++;
    }
    for(int i=0; i<2; i++){
        for(int j=0; j<6; j++){
            if(arry[i][j]!=0) sum+=arry[i][j] / k;
            if(arry[i][j]%k!=0) sum++;
        }
    }
    printf("%d\n",sum);


    return 0;
}