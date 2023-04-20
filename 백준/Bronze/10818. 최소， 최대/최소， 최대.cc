#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin>>n;
    
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin>>nums[i];
    }

    int min = *min_element(nums.begin(), nums.end());
    int max = *max_element(nums.begin(), nums.end());

    cout<<min<< " " <<max<<"\n";
    return 0;
}