#include<bits/stdc++.h>

using namespace std;

int getMedian(int arr[], int n) {
    int med;
    
    if (n % 2 == 0) med = (arr[n / 2] + arr[n / 2 - 1]) / 2;
    else med = arr[n / 2];
    
    return med;
}
int min(int a, int b) {
    if (a < b) return a;
    else return b;
}
int max(int a, int b) {
    if (a > b) return a;
    else return b;
}
bool itsEven(int a) {
    if (a % 2 == 0) return true;
    else return false;
}
double medianTwoSortedArrays(int A[], int B[], int n) {
    if (n == 1) return(double)((A[0] + B[0]) / 2.0);
    if (n == 2) return (double)((max(A[0], B[0]) + min(A[1], B[1])) / 2.0);
    
    int medA = getMedian(A, n);
    int medB = getMedian(B, n);
    if (medA == medB) return medA;
    
    if (medA < medB) {
        if (itsEven(n)) return medianTwoSortedArrays(A + n / 2 - 1, B, n - n / 2 + 1);
        else return medianTwoSortedArrays(A + n / 2, B, n - n / 2);
    }
    if (itsEven(n)) return medianTwoSortedArrays(B + n / 2 - 1, A, n - n / 2 + 1);
    else return medianTwoSortedArrays(B + n / 2, A, n - n / 2);
}

int main() {
    int n;
    cin >> n;
    
    int A[n], B[n];
    for (int i = 0; i < n; i++) cin >> A[i];
    for (int i = 0; i < n; i++) cin >> B[i];
    
    cout << medianTwoSortedArrays(A, B, n) << endl;
    return 0;
}
