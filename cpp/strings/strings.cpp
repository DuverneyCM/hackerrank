/*
Sample Input:
abcd
ef
Sample Output:
4 2
abcdef
ebcd af
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;
    char a0, b0;
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl;
    cout << a+b << endl;
    a0 = a[0]; b0 = b[0];
    a[0] = b0; b[0] = a0;
    cout << a << " " << b;
    
    return 0;
}