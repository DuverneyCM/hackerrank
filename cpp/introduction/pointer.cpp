/*
Sample Input:
4
5
Sample Output:
9
1
*/

#include <stdio.h>

void update(int *a,int *b) {
    // Complete this function    
    int sum, res;
    sum = *a + *b;
    if(*a > *b) res = *a - *b;
    else res = *b - *a;
    *a = sum;
    *b = res;
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}