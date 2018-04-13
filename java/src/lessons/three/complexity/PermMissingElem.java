package lessons.three.complexity;

public class PermMissingElem {

	public PermMissingElem() {
	}

	public int solution(int[] A) {
		int N = A.length + 1;
		int sumN = (1 + N) * N / 2;
		
		for (int i = 0; i < A.length; i++) {
			sumN -= A[i];
		}
		
		return sumN;
	}
}
