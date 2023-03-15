#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<int> y(n);
    for(int i=0; i<n; i++){
        cin>>y[i];        
    }
    sort(y.begin(), y.end());    
    if(n==1) cout<<y[0]*y[0]<<endl;
    else cout<<y[0]*y[n-1]<<endl;

    return 0;
}