#include <iostream>
#include <ctime> // para as medições de tempo de CPU (CPU Time)

using namespace std;

bool itsSorted(int array[], int n) {
    for (int i = 1; i < n; i++) if (array[i - 1] > array[i] ) return false;
    return true;
}

void printArrayLongDouble(long double array[], int n) {
    for (int i = 0; i < n; i++) cout << array[i] << '\t';
    cout << endl;
    return;
}
void printArrayInt(int array[], int n) {
    for (int i = 0; i < n; i++) cout << array[i] << '\t';
    cout << endl;
    return;
}

void insertionSort(int array[], int n) {
    int num, j;
    
    for (int i = 1; i < n; i++) {
        num = array[i];
        for (j = i - 1; j > -1; j--) {
            if (array[j] > num) array[j + 1] = array[j];
            else break;
        } array[j + 1] = num;
    }
    
    return;
}

void merge(int array[], int li, int mi, int ri) {
    int n1 = mi - li + 1;
    int n2 = ri - mi;
    int left[n1], right[n2];
    
    for (int i = 0; i < n1; i++) left[i] = array[li + i];
    for (int j = 0; j < n2; j++) right[j] = array[mi + 1 + j];
    
    int i = 0, j = 0, k = li;
    
    while (i < n1 and j < n2) {
        if (left[i] <= right[j]) {
            array[k] = left[i];
            i++;
        }
        else {
            array[k] = right[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        array[k] = left[i];
        i++;
        k++;
    }
    while (j < n2) {
        array[k] = right[j];
        j++;
        k++;
    }
    
    return;
}
void mergeSort(int array[], int li, int ri){
    if(li >= ri) return;

    int mi = li + (ri - li) / 2;
    mergeSort(array, li, mi);
    mergeSort(array, mi + 1, ri);
    merge(array, li, mi, ri);
}

void copy(int array_ori[], int array_copy[], int n) {
    for (int i = 0; i < n; i++) array_copy[i] = array_ori[i];
    return;
}

int main() {
    int n_test_case = 12, j = 0, len;
    
    long double insertionSort_times[n_test_case];
    long double mergeSort_times[n_test_case];
    
    std::clock_t c_start, c_end;
    long double time_elapsed_ms;
    
    int lens[n_test_case] = {10, 20, 30, 40, 100, 200, 300, 400, 1000, 2000, 3000, 4000}; // n_test_case = 12 == len(lens)
    for (int i = 0; i < n_test_case; i++) {
        len = lens[i];
        int array[len], array_copy[len];;
        
        // criando caso de test
        int p = -1;
        for (int z = len - 1; z > -1; z--) array[++p] = z;
        
        copy(array, array_copy, len);
        // insertion sort
        c_start = std::clock();
        insertionSort(array_copy, len);
        c_end = std::clock();
        
        time_elapsed_ms = 1000.0 * (c_end-c_start) / CLOCKS_PER_SEC;
        insertionSort_times[j] = time_elapsed_ms;
        // verifica se ordenou mesmo
        if (not itsSorted(array_copy, len)) cout << "insertionSort() no " << "caso de test" << j + 1 << ", failed" << endl;
        
        copy(array, array_copy, len);
        // merge sort
        c_start = std::clock();
        mergeSort(array_copy, 0, len - 1);
        c_end = std::clock();
        
        time_elapsed_ms = 1000.0 * (c_end-c_start) / CLOCKS_PER_SEC;
        mergeSort_times[j] = time_elapsed_ms;
        // verifica se ordenou mesmo
        if (not itsSorted(array_copy, len)) cout << "mergeSort() no " << "caso de test" << j + 1 << ", failed" << endl;
        
        j++;
    }
    
    cout << "Nas seguintes quantidades de elementos no array:" << endl << "CPU time in ms for insertionSort: " << endl << "CPU time in ms for mergeSort: " << endl;
    printArrayInt(lens, n_test_case);
    printArrayLongDouble(insertionSort_times, n_test_case);
    printArrayLongDouble(mergeSort_times, n_test_case);
    return 0;
}
