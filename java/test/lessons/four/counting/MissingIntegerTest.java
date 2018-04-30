package lessons.four.counting;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class MissingIntegerTest {
	MissingInteger mi = new MissingInteger();
	
	@Test
	void test() {
		assertAll(
			() -> assertEquals(5, mi.solution(new int[] { 1, 3, 6, 4, 1, 2 })),
			() -> assertEquals(4, mi.solution(new int[] { 1, 2, 3 })),
			() -> assertEquals(1, mi.solution(new int[] { -1, -3 }))
		);
	}

}
