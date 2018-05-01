package lessons.five.prefix.sums;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class CountDivTest {
	private CountDiv cd = new CountDiv();

	@Test
	void test() {
		
		assertAll(
			() -> assertEquals(3, cd.solution(6, 11, 2)),
			() -> assertEquals(1, cd.solution(6, 6, 2)),
			() -> assertEquals(0, cd.solution(11, 11, 2))
		);
		
	}
	
	@Test
	void testSimple() {
		assertAll(
			() -> assertEquals(1, cd.solution(11, 13, 2)),
			() -> assertEquals(3, cd.solution(2, 6, 2)),
			() -> assertEquals(4, cd.solution(2, 9, 2))
		);
		
	}
	
	@Test
	void testPerformance() {
		
		assertAll(
			() -> assertEquals(61728345, cd.solution(100, 123456789, 2)),
			() -> assertEquals(12345, cd.solution(101, 123456789, 10000)),
			() -> assertEquals(2000000001, cd.solution(0, 2000000000, 1)),
			() -> assertEquals(2, cd.solution(0, 2000000000, 2000000000))
		);
		
	}

}
