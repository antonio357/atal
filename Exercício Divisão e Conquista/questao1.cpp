#include <iostream>

using namespace std;

int maxNum(int a, int b, int c) {
    int array[3] = {a, b, c};
    int max = array[0];
    for (int i = 1; i < 3; i++) if (array[i] > max) max = array[i];
    return max;
}
int mergeSum(const int array[], int i, int f) {
    int max_left = 0, max_right = 0, m = (i + f) / 2, sum;
    
    sum = 0;
    for (int j = m; j >= i; j--) {
        sum += array[j];
        if (sum > max_left) max_left = sum;
    }
    
    sum = 0;
    for (int j = m + 1; j <= f; j++) {
        sum += array[j];
        if (sum > max_right) max_right = sum;
    }
    
    return max_left + max_right;
}
int maxSubArraySum(const int array[], int i, int f) {
    if (i == f) return array[i];
    else {
        int m = (i + f) / 2;
        int left = maxSubArraySum(array, i, m);
        int right = maxSubArraySum(array, m + 1, f);
        int middle = mergeSum(array, i, f);
        return maxNum(left, right, middle);
    }
}

int main() {
    int n, max;
    
    while (true) {
        cin >> n;
        if (n == 0) break;
        
        int array[n];
        for (int i = 0; i < n; i++) cin >> array[i];
        
        max = maxSubArraySum(array, 0, n - 1);
        if (max > 0) cout << "The maximum winning streak is " << max << '.' << endl;
        else cout << "Losing streak." << endl;
    }
    
    return 0;
}
