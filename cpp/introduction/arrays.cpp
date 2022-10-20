/*
Sample Input:
4
1 4 3 2
Sample Output:
2 3 4 1
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int n;
    cin >> n;
    
    int intList[n];
    for(int i=0; i<n; i++) scanf("%d", intList+i); //cin >> intList[i];
    for(int j=1; j<=n; j++) cout << intList[n-j] << " ";

    return 0;
}