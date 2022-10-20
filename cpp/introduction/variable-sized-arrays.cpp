/*
Sample Input:
2 2
3 1 5 4
5 1 2 8 9 3
0 1
1 3
Sample Output:
5
9
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    //https://www.techiedelight.com/dynamic-memory-allocation-in-c-for-2d-3d-array/
    int n, q, i, j, k;
    cin >> n >> q;
    int** a = new int*[n];
    //int a[n][300000];
    
    for (int i=0; i<n; i++) {
        cin >> k;
        a[i] = new int[k];
        //int b[k];
        //int *b = new int[k];
        //a[i] = b;
        for (int j=0; j<k; j++) {
            //cin >> b[j];
            cin >> a[i][j]; 
            //cout << *(a[i]+j) <<" "<< &b[j] << endl;
        }
    }
    
    for (int k=0; k<q; k++) {
        cin >> i >> j;
        //cout << *(a[x]+y) << endl;
        //cout << i << j << endl;
        //cout << *(a[i]) << endl;
        cout << a[i][j] << endl;
    }
    return 0;
}
