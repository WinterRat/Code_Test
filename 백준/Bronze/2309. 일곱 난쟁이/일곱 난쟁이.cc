#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
    int t[9];
    int sum=0;
    for(int i=0; i<9; i++){
        scanf("%d",&t[i]);
        sum += t[i];
    }
    for(int i=0; i<8; i++){
        for(int j=i+1; j<9; j++){
            if(sum-t[i]-t[j] == 100){
                t[i]=101;
                t[j]=101;
                sort(t,t + 9);
                break;
            }
        }
        if(t[8]==101) break;    
    }
    for(int k=0; k<7; k++) printf("%d\n",t[k]);    
    return 0;
}