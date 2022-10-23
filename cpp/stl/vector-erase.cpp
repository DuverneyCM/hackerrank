/*
Sample Input:
6
1 4 6 2 8 9
2
2 4
Sample Output:
3
1 8 9
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N;
    cin >> N;

    vector<long long int>v;
    long long int b;
    for(int i = 0; i < N; i++){
        cin >> b;
        v.push_back(b);
    }
    
    int q1,q2;
    cin >> q1;
    v.erase(v.begin() + (q1 - 1));
    cin >> q1;
    cin >> q2;
    v.erase(v.begin() + (q1 - 1), v.begin() + (q2 - 1));

    cout << v.size() << endl;
    for(int elem: v){
        cout << elem << " ";
    }

    return 0;
}