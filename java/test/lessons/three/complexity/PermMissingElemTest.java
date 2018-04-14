package lessons.three.complexity;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * https://app.codility.com/demo/results/training5M2Q7Z-6JB/
 * 
 * @author Luis
 */
class PermMissingElemTest {

	PermMissingElem pme = new PermMissingElem();

	@Test
	void test() {
		assertAll(
				() -> assertEquals(4, pme.solution(new int[] { 1, 2, 3, 5 })),
				() -> assertEquals(1, pme.solution(new int[] { 2, 3, 4, 5, 6 }))
		);
	}
	
	@Test
	void largeRangeTest() {
		final int[] array = new int[100_000];
		final int[] array2 = new int[100_000];
		
		for (int i = 0, j = 0; i < array2.length; i++, j++) {
			array[i] = i + 2;
			
			if (j == 100_000) {
				j++;
			}
			array2[i] = j + 1;
		}
		
		assertAll(
				() -> assertEquals(1, pme.solution(array)),
				() -> assertEquals(100_001, pme.solution(array2))
		);
	}

}
