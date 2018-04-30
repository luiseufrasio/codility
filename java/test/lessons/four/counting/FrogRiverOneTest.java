package lessons.four.counting;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class FrogRiverOneTest {
	private FrogRiverOne fro = new FrogRiverOne();

	@Test
	void test() {
		final int X = 100000;
		int[] A = new int[X];
		for (int i = 0; i < A.length; i++) {
			A[i] = i + 1;
		}
		
		assertAll(
			() -> assertEquals(6, fro.solution(5, new int[] { 1, 3, 1, 4, 2, 3, 5, 4 })),
			() -> assertEquals(-1, fro.solution(5, new int[] { 1, 3, 1, 4 })),
			() -> assertEquals(99999, fro.solution(X, A))
		);
	}

}
