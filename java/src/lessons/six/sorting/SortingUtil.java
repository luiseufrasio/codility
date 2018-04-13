package lessons.six.sorting;

public class SortingUtil {

	public SortingUtil() {
	}

	static int[] randomArray(int N) {
		return randomArray(N, 100);
	}
	
	static int[] randomArray(int N, int k) {
		int[] A = new int[N];
		
		for (int i = 0; i < A.length; i++) {
			A[i] = (int) (Math.random() * k);
		}
		
		return A;
	}
}
