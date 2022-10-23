/*
Sample Input:
2
5 2
3 4 6 3 4
7 4
3 4 5 8 1 4 10
Sample Output:
4 6 6 4
8 8 8 10
*/

#include <iostream>
#include <deque> 
using namespace std;

void printKMax(int arr[], int n, int k){
	//Write your code here.
    deque<int> q;
    for(int i = 0; i < n; i++) {
        
        while(!q.empty() && arr[i] > q.back())
            q.pop_back();  
        q.push_back(arr[i]);  
        if(i >= k && q.front() == arr[i-k])
            q.pop_front();  
        if(i >= k-1)
            printf(i < n-1 ? "%d ":"%d\n", q.front());
    }
}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}