// given an unordered array and a pivot value as the last element in the array, sort the array such that all elements smaller than pivot appear at the left of the pivot.

// use j to iterate the array, till meet k.
// < i left is elements smaller than pivot; 
//  [i, j) is pivots duplicate;
// (k, -1] is elements greater then pivot;
void partition(vector<int> A) {
  int i = 0, j = 0, k = A.size() - 1, pivot = A[A.size() - 1];
  while(j < k) {
    if (A[j] < pivot) {
      swap(A, i, j);
      i++;
      j++;
    }
    else if (A[j] == pivot) {
      swap(A, j, k);
      k--;
    }
    else { // A[j] > pivot
      j++;
    }
  }
}

// Extensions: find kth-largest element in the array, using idea of partition: find a pivot and arrange elements with the pivot.
// a good follow up question: whether elements are unique or can have duplicates.
int find_element(vector<int> A, int k) {
  int pivot = A[A.size() - 1]; // assume the pivot is the last element.
  int pivot_index = partition(A, pivot);
  if (pivot_index == k - 1) {
    return pivot;
  }
  else if (pivot_index < k) {
    vector<int> R(A.begin() + pivot_index, A.begin() + A.size() - 1); // construct sub-vector from a vector.
    find_element(R, k - pivot_index - 1);
  }
  else {
    vector<int> L(A.begin() + 0, A.begin() + pivot_index);
    find_element(L, k);
  }
}

// assuming all elments are distinct.
int partititon(vector<int> A, int pivot) {
  int i = 0, j = 0;
  while(j < A.size()) {
    if (A[j] < pivot) {
      swap(&A[i], &A[j]);
      i++;
      j++;
    }
    else{ // A[j] > pivot
      j++;
    }
  }
  swap(&A[i], &A[A.size() - 1]);
  return i;
}

void swap(int* a, int* b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}