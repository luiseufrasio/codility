package lessons.six.sorting;

import java.util.Arrays;

public class CountingSort {

	public CountingSort() {
	}
	
	public void sort(int[] A, int k) {
		int N = A.length;
		int[] count = new int[k + 1];
		Arrays.setAll(count, (i) -> 0);
		
		for (int i = 0; i < N; i++) {
			count[A[i]]++;
		}
		System.out.println("count=" + Arrays.toString(count));
		
		int p = 0;
		for (int i = 0; i <= k; i++) {
			for (int j = 0; j < count[i]; j++) {
				A[p] = i;
				p++;
			}
		}
	}
	
	public static void main(String[] args) {
		final int k = 100;
		int[] A = SortingUtil.randomArray(10, k);
		
		//System.out.println("original A=" + Arrays.toString(A));
		new CountingSort().sort(A, k);
		//System.out.println("ordered A=" + Arrays.toString(A));
	}

}