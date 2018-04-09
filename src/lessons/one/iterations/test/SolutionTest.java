package lessons.one.iterations.test;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

import lessons.one.iterations.Solution;

class SolutionTest {
	Solution s = new Solution();

	@Test
	void test() {
		assertAll(
			() -> assertEquals(2, s.solution(9)),
			() -> assertEquals(4, s.solution(529)),
			() -> assertEquals(1, s.solution(20)),
			() -> assertEquals(0, s.solution(15))
		);
	}

}
