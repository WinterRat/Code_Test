#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool check(string password){
    int vowel = 0, consonant = 0; // 모음 , 자음
    for(char c : password){
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') vowel++;
        else consonant++;       
    }
    //if(vowel >= 1 && consonant >= 2) return true;
    return vowel >= 1 && consonant >= 2;
}
void check_print(int L, vector<char> &alpha, string password, int i){
    if(password.length() == L){
        if(check(password)){
            cout<<password<<endl;
        }
        return;
    }
    if(i >= alpha.size()){
        return;
    }
    check_print(L, alpha, password + alpha[i], i+1);
    check_print(L, alpha, password, i+1);
}

int main() {
    int L, c;
    cin>>L>> c;
    vector<char> alpha(c);
    for (int i = 0; i < c; i++){
        cin>>alpha[i];
    }
    sort(alpha.begin(), alpha.end());
    check_print(L, alpha, "", 0);
    return 0;
}