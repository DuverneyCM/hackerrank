/*
Sample Input:
5
1 6 10 8 4
Sample Output:
1 4 6 8 10
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int N, elem;
    cin >> N;
    vector<int> v;
    for (int i=0; i<N; i++) {
        cin >> elem;
        v.push_back(elem);
    }
    sort(v.begin(),v.end());
    for (int i=0; i<N; i++) {
        cout << v.front() << " ";
        v.erase(v.begin());
    }
    return 0;
}