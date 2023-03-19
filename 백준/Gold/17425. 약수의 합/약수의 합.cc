#include <stdio.h>
int f[1000001];
long long s[1000001]; //1~1,000,000까지 자연수들의 "약수의 총합"의 총합
int main()
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=1000000;i++){
        for(int j=i;j<=1000000;j+=i) f[j]+=i;
    }
    for(int i=1;i<=1000000;i++) s[i]=s[i-1]+f[i]; 
    while(T--){
        int v;
        scanf("%d",&v);
        printf("%lld\n",s[v]);
    }
    return 0;
}