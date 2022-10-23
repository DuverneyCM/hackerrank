/*
Sample Input:
8
1 9
1 6
1 10
1 4
3 6
3 14
2 6
3 6
Sample Output:
Yes
No
No
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N, value, code;
    cin >> N;
    set<int> s;
    set<int>::iterator itr;
    for (int i=0; i<N; i++) {
        cin >> code >> value;
        if (code == 1)
            s.insert(value);
        else if (code == 2)
            s.erase(value);
        else if (code == 3) {
            if (s.find(value) != s.end())
                cout << "Yes " << endl;
            else
                cout << "No " << endl;
        }
    }
    return 0;
}