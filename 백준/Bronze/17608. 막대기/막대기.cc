#include <stdio.h>
#include <vector>
using namespace std;
int main()
{
    int n, max, now=0;
    int count = 1;
    scanf("%d",&n);
    vector <int> v(n);
    for(int i=0; i<n; i++){
        scanf("%d",&v[i]);     
    }
    max = v[n-1];
    for(int i=0; i<n; i++){
        now = v.back();
        v.pop_back();
        if(max<now){
            max = now;
            count ++;
        }
    }
    printf("%d\n",count);
    return 0;
}