package lessons.six.sort;

import java.util.Arrays;

public class SelectionSort {

	public SelectionSort() {
	}
	
	public void sort(int[] A) {
		int N = A.length;
		for (int k = 0; k < N; k++) {
			int minimal = k;
			for (int j = k + 1; j < N; j++) {
				if (A[j] < A[minimal]) {
					minimal = j;
				}
			}
			int l = A[k];
			A[k] = A[minimal];
			A[minimal] = l;
		}
	}
	
	public static void main(String[] args) {
		int[] A = SortingUtil.randomArray(100000);
		
		System.out.println("original A=" + Arrays.toString(A));
		new SelectionSort().sort(A);
		System.out.println("ordered A=" + Arrays.toString(A));
	}
	
	

}