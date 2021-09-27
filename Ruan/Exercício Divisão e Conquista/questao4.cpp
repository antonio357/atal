#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int quickSelect(int array[], int i, int f, int k) {
    int d = i, aux;
    int p = array[f];
    
    for (int j = i; j <= f - 1; j++) {
        if (array[j] <= p) {
            aux = array[j];
            array[j] = array[d];
            array[d] = aux;
            d++;
        }
    }
    aux = array[f];
    array[f] = array[d];
    array[d] = aux;
    
    if (d - i == k - 1) return p;
    else if (d - i > k - 1) return quickSelect(array, i, d - 1, k);
    else return quickSelect(array, d + 1, f, k - d + i - 1);
}

int list1[3] = {4, -2, 6};
int list2[10] = {7, 2, 3, 1, 0, 2, 8, 4, -3, 6};
int list3[1] = {-7};
int list4[10] = {0, -5, -7, -10, -5, -8, 10, 7, -2, 3};
int list5[4] = {-7, -4, 8, 6};
int* lists[5] = {list1, list2, list3, list4, list5};

int lens[5] = {3, 10, 1, 10, 4};
int ks[5] = {2, 4, 1, 8, 3};

int main() {
    int n, k, n_casos_test = 5, r;
    
    for (int i = 0; i < n_casos_test; i++) {
        n = lens[i];
        k = ks[i];
        
        r = quickSelect(lists[i], 0, n - 1, k);
        sort(lists[i], lists[i] + n); // ordenando o vetor para conferir com o resultado esperado
        
        // conferindo se o resultado é o esperado
        if (r != lists[i][k - 1]) cout << "resposta deveria ser " << lists[i][k - 1] << ", mas foi" << "k" << endl;
        else cout << r << endl;
    }

    return 0;
}
