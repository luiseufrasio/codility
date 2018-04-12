package lessons.six.sorting;

public class SortingUtil {

	public SortingUtil() {
	}

	static int[] randomArray(int N) {
		int[] A = new int[N];
		
		for (int i = 0; i < A.length; i++) {
			A[i] = (int) (Math.random() * 100);
		}
		
		return A;
	}
}
