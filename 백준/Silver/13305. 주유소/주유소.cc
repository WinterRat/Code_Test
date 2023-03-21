#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n; 

    cin>>n;
    vector<long long> dist(n-1);
    vector<long long> cost(n);
    for(int i=0; i<n-1; i++){
        cin>>dist[i]; 
    }
    for(int j=0; j<n; j++){ 
        cin>>cost[j];
    }
    long long now=cost[0];
    long long tot_c=0;

    for(int i=0; i<n-1; i++){
        now = min(now,cost[i]);
        tot_c += now*dist[i];
    }
    cout<<tot_c<<'\n';
    return 0;
}