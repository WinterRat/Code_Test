#include <iostream>
using namespace std;

bool is_prime(int n){
	if(n < 2) return false;
	for(int i=2; i*i<=n; i++){
		if (n % i == 0) return false;
	}
	return true;
}

int main()
{
	int a,b;
    int count = 0;
    cin>>a;
    for(int i=0; i<a; i++){
        cin>>b;
        if(is_prime(b)) count++;
    }
    cout<<count<<endl;
    return 0;
}