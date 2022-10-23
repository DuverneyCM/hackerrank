/*
Sample Input:
7
1 Jesse 20
1 Jess 12
1 Jess 18
3 Jess
3 Jesse
2 Jess
3 Jess
Sample Output:
30
20
0
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, valueY, lastValue, code;
    string keyX;
    cin >> N;
    map<string, int> m;
    map<string, int>::iterator itr;
    for (int i=0; i<N; i++) {
        cin >> code;
        if (code == 1) {
            cin >> keyX >> valueY;
            if (m.find(keyX) == m.end()) {
                m.insert(make_pair(keyX, valueY));
            }
            else {
                lastValue = m.find(keyX)->second;
                m.erase(keyX);
                m.insert(make_pair(keyX, valueY + lastValue));
            }
        }
        else if (code == 2) {
            cin >> keyX;
            m.erase(keyX);
        }
        else if (code == 3) {
            cin >> keyX;
            cout << m[keyX] << endl;
        }
    }
    return 0;
}