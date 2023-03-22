#include <iostream>
#include <stack>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N;
    cin>>N;

    stack<int> s;
    int max = 0;

    for (int i = 0; i < N; i++) {
        int h;
        cin>>h;

        while (!s.empty() && s.top() <= h) {
            s.pop();
        }
        s.push(h);
    }
    cout<<s.size()<<'\n';
    return 0;
}