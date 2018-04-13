package lessons.three.complexity;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;


/**
 * https://app.codility.com/demo/results/trainingJP3UW9-GMR/
 * 
 * @author Luis
 *
 */
class FrogJumpTest {
	FrogJump fj = new FrogJump();
	
	@Test
	void testExamples() {
		assertAll(
				() -> assertEquals(3, fj.solution(10, 85, 30)),
				() -> assertEquals(4, fj.solution(1, 8, 2))
		);
	}
	
	@Test
	void testSmallJumps() {
		assertAll(
				() -> assertEquals(142730189, fj.solution(3, 999111321, 7)),
				() -> assertEquals(500_000_000, fj.solution(1, 1_000_000_000, 2))
		);
	}

}
