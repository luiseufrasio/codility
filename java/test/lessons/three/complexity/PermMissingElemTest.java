package lessons.three.complexity;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

/**
 * https://app.codility.com/demo/results/trainingP8NAFU-YD6/
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
		final int[] array = new int[10];
		final int[] array2 = new int[10];
		
		for (int i = 0, j = 0; i < array.length; i++, j++) {
			array[i] = i + 1;
			
			if (j == 5) {
				array2[j] = j + 2;
				j++;
			} else if (j < array2.length) {
				array2[j] = j + 1;
			}
		}
		
		assertAll(
				() -> assertEquals(1, pme.solution(array)),
				() -> assertEquals(5, pme.solution(array2))
		);
	}

}
