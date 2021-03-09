#include <iostream>
#include <ctime> // para as medições de tempo de CPU (CPU Time)

using namespace std;

// verifica se um array esta ordenado
bool itsSorted(int array[], int n) {
    for (int i = 1; i < n; i++) if (array[i - 1] > array[i] ) return false;
    return true;
}

// printa um array de long double
void printArrayLongDouble(long double array[], int n) {
    for (int i = 0; i < n; i++) cout << array[i] << '\t';
    cout << endl;
    return;
}
// printa um array de int
void printArrayInt(int array[], int n) {
    for (int i = 0; i < n; i++) cout << array[i] << '\t';
    cout << endl;
    return;
}
// ordena em o(n²)
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
// uni dois arrays ordenados em um array ordenado
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
// ordenação em O(nlog2(n))
void mergeSort(int array[], int li, int ri){
    if(li >= ri) return;

    int mi = li + (ri - li) / 2;
    mergeSort(array, li, mi);
    mergeSort(array, mi + 1, ri);
    merge(array, li, mi, ri);
}
// faz uma copia de um array
void copy(int array_ori[], int array_copy[], int n) {
    for (int i = 0; i < n; i++) array_copy[i] = array_ori[i];
    return;
}

int main() {
    // n_test_case, quantidade de casos de test
    // len, tamanho do array do caso de teste atual
    // j, dita o index do caso de teste atual, para armazenar o tempo deste em insertionSort_times e mergeSort_times
    int n_test_case = 12, j = 0, len;
    
    // armazena as medições de tempo
    long double insertionSort_times[n_test_case];
    long double mergeSort_times[n_test_case];
    // para medição de tempo
    std::clock_t c_start, c_end;
    long double time_elapsed_ms;
    
    // tamanhos dos array dos casos de teste
    int lens[n_test_case] = {10, 20, 30, 40, 100, 200, 300, 400, 1000, 2000, 3000, 4000}; // n_test_case = 12 == len(lens)
    for (int i = 0; i < n_test_case; i++) {
        len = lens[i];
        // array, caso de teste atual
        /* array_copy, é uma cópia de array, que é ordenada ao em vez de array
        já que a ordenação será feita para o insertionSort e depois para o mergeSort */
        int array[len], array_copy[len];
        
        // criando caso de test atual
        int p = -1;
        for (int z = len - 1; z > -1; z--) array[++p] = z;
        
        // fazendo backup do caso de teste atual
        copy(array, array_copy, len);
        // insertion sort
        c_start = std::clock(); // inicio da medição do tempo
        insertionSort(array_copy, len); // ordenação por insertion sort
        c_end = std::clock(); // final da medição do tempo
        
        // tempo da execução do insertion sort em ms
        time_elapsed_ms = 1000.0 * (c_end - c_start) / CLOCKS_PER_SEC; 
        /* ao dividir por CLOCKS_PER_SEC obtemos o tempo
        ao mutiplicar por 1000.0 convetemos o tempo obtido para ms */
        insertionSort_times[j] = time_elapsed_ms;
        // verifica se ordenou mesmo a copia do caso de teste atual
        if (not itsSorted(array_copy, len)) cout << "insertionSort() no " << "caso de test" << j + 1 << ", failed" << endl;
        
        // usando o backup do caso de teste atual para desordenar o caso de teste atual
        copy(array, array_copy, len);
        // merge sort
        c_start = std::clock(); // inicio da medição do tempo
        mergeSort(array_copy, 0, len - 1); // ordenação por merge sort
        c_end = std::clock(); // final da medição do tempo
        
        // tempo da execução do merge sort em ms
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
