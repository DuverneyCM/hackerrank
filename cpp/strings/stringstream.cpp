/*
Sample Input:
23,4,56
Sample Output:
23
4
56
*/

#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
	// Complete this function
    stringstream ss(str);
    string number;
    vector<int> numberlist;
    while(getline(ss, number, ',')){
        numberlist.push_back(stoi(number));
    }
    return numberlist;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}
