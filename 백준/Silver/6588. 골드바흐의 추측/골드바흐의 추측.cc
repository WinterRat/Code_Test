#include <stdio.h>
#include <vector>
using namespace std;

const int MAX = 1000000; 
bool check[MAX+1];
vector<int> prime;

void make_prime() { // 소수풀 만들기
    for(int i=2; i<=MAX; i++) {
        if(check[i] == false) {
            prime.push_back(i);
            for(int j=i*2; j<=MAX; j+=i) {
                check[j] = true;
            }
        }
    }
}
void check_print(int n) { // 위대한 수학자가 맞겠지머 
    for(int i=0; i<prime.size(); i++) {
        int p = prime[i];
        if(check[n-p] == false) {
            printf("%d = %d + %d\n",n,p,n-p);
            return;
        }
    }
}
int main() {

    make_prime();
    int n;
    while(scanf("%d",&n)) {
        if(n==0) break;
        check_print(n);
    }
    return 0;
}