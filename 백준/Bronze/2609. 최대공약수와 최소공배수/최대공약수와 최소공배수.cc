#include <iostream>
#include <vector>

using namespace std;
//유클리드 호제법
int gcd(int a, int b)
{
	int c;
	while (b != 0)
	{
		c = a % b;
		a = b;
		b = c; //나머지가 0이 될 때
	}
	return a;
}
int lcm(int a, int b)
{
    return a * b / gcd(a, b);
}
int main()
{
    int n, m;

    cin>>n>>m;
    
    cout<<gcd(n,m)<<endl;
    cout<<lcm(n,m)<<endl;

    return 0;
}