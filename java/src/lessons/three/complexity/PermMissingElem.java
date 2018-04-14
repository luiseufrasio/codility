package lessons.three.complexity;

public class PermMissingElem {

	public PermMissingElem() {
	}

	public int solution(int[] A) {
		int N = A.length + 1;
		double sumN = (1.0 + N) * N / 2.0 ;
		
		for (int i = 0; i < A.length; i++) {
			sumN -= A[i];
		}
		
		return (int) sumN;
	}
	
}