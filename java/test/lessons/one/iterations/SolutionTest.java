package lessons.one.iterations;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import lessons.one.iterations.Solution;

/**
 * Final Result:
 * https://app.codility.com/demo/results/trainingP76KZ2-HTY/
 * 
 * @author Luis Eufrasio
 *
 */
class SolutionTest {
	Solution s = new Solution();

	@Test
	void exampleTests() {
		assertAll(
			() -> assertEquals(5, s.solution(1041)),
			() -> assertEquals(0, s.solution(15))
		);
	}
	
	@Test
	void extremeTests() {
		assertAll(
			() -> assertEquals(0, s.solution(1)),
			() -> assertEquals(1, s.solution(5)),
			() -> assertEquals(0, s.solution(2147483647))
		);
	}
	
	@Test
	void trailingZeroesTests() {
		assertAll(
			() -> assertEquals(0, s.solution(16)),
			() -> assertEquals(1, s.solution(5)),
			() -> assertEquals(0, s.solution(1024))
		);
	}
	
	@Test
	void largeTests() {
		assertAll(
			() -> assertEquals(20, s.solution(6291457)),
			() -> assertEquals(4, s.solution(74901729)),
			() -> assertEquals(25, s.solution(805306373)),
			() -> assertEquals(5, s.solution(1376796946)),
			() -> assertEquals(29, s.solution(1073741825)),
			() -> assertEquals(28, s.solution(1610612737))
		);
	}

}
