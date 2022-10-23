/*
Sample Input:
 8
 1 1 2 2 6 9 9 15
 4
 1
 4
 9
 15
Sample Output:
 Yes 1
 No 5
 Yes 6
 Yes 8
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int N;
    cin >> N;

    vector<long long int>v;
    long long int b;
    for(int i = 0; i < N; i++){
        cin >> b;
        v.push_back(b);
    }
    
    vector<long long int>::iterator low;
    int Q, n, pos;
    cin >> Q;
    for(int i = 0; i < Q; i++) {
        cin >> n;
        low = lower_bound(v.begin(), v.end(), n);
        pos = (low - v.begin() + 1);
        if (*low == n)
            cout << "Yes " << pos << endl;
        else
            cout << "No " << pos << endl;
        
    }
    return 0;
}
