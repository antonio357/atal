#include<bits/stdc++.h>

using namespace std;

typedef struct {
    double val;
    int i;
} median;

void printArray(int array[], int left, int right) {
    for (int j = left; j <= right; j++) cout << array[j] << ' ';
    cout << endl;
}

median getMedian(int array[], int left, int right, bool goCenter, bool leftArray) {
    median med = {-1.0, -1};
    int len = (right - left + 1);
    
    bool odd = false;
    if (len % 2 != 0) odd = true;
    
    int m;
    if (goCenter) {
        if (leftArray) m = (len / 2) + left;
        else {
            if (odd) m = (len / 2) + left;
            else m = (len / 2) - 1;
        }
    }
    else {
        if (leftArray) {
            if (odd) m = (len / 2) + left;
            else m = (len / 2) + (right - left);
        }
        else m = (len / 2) + left;
    }

    med.val = array[m];
    med.i = m;
    
    cout << "left, right = " << left << ", " << right;
    cout << ", len = " << len << ", odd = " << odd << ", m = " << m << ", val = " << med.val << endl;
    
    return med;
}
void medianTwoSortedArrays(int A[], int B[], int leftA, int rightA, int leftB, int rightB, int counter, bool goCenter) {
    counter++;
    if (counter >= 40) return;
    cout << "medianTwoSortedArrays" << endl;
    printArray(A, leftA, rightA); printArray(B, leftB, rightB);
    
    int len = rightA - leftA + 1;
    if (len == 1) {
        cout << "worked, leftA, leftB = " << leftA << ", " << leftB << endl;
        cout << (A[leftA] + B[leftB]) / 2.0 << endl;
        return;
    }
    
    median medianA = getMedian(A, leftA, rightA, goCenter, true);
    median medianB = getMedian(B, leftB, rightB, goCenter, false);
    double final_median;
    
    if (medianA.val == medianB.val) final_median = medianA.val;
    else {
        if (medianA.val < medianB.val) {
            cout << "going center" << endl;
            medianTwoSortedArrays(A, B, medianA.i, rightA, leftB, medianB.i, counter, true);
        }
        else {
            cout << "going edge" << endl;
            medianTwoSortedArrays(A, B, leftA, medianA.i, medianB.i, rightB, counter, false);
        }
    }
    
    //cout << (A[leftA] + B[leftB]) / 2.0 << endl;
    return;
}

int main() {
    int a[] = {1, 12, 15, 26, 38};
    int b[] = {2, 13, 17, 30, 45};
    //int a[] = {1, 2, 3, 4, 5};
    //int b[] = {6, 7, 8, 9, 10};
    int n = sizeof(a) / sizeof(int);
    
    int counter = 0;
    medianTwoSortedArrays(a, b, 0, n - 1, 0, n - 1, counter, true);
    return 0;
}
