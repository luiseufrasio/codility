package lessons.four.counting;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class MaxCountersTest {
	private MaxCounters mc = new MaxCounters();
	
	@Test
	void test() {
		assertAll(
			() -> assertArrayEquals(
					new int[] {10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10}, 
					mc.solution(100, new int[] {14, 32, 14, 51, 60, 85, 91, 99, 24, 28, 14, 3, 22, 101, 99, 2, 70, 19, 91, 64, 18, 10, 101, 68, 53, 42, 78, 28, 13, 47, 37, 101, 67, 12, 27, 101, 17, 101, 101, 77, 24, 42, 101, 40, 14, 4, 101, 13, 101, 101})	
				),
			() -> assertArrayEquals(
					new int[] {3}, 
					mc.solution(1, new int[] {2, 1, 1, 2, 1})	
				),
			() -> assertArrayEquals(
				new int[] {3, 2, 2, 4, 2},
				mc.solution(5, new int[] {3, 4, 4, 6, 1, 4, 4})
			),
			() -> assertArrayEquals(
				new int[] {9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9}, 
				mc.solution(20, new int[] {21, 7, 14, 21, 14, 21, 18, 5, 5, 21, 14, 7, 6, 21, 6, 14, 18, 15, 4, 10, 19, 5, 10, 10, 12, 10, 17, 4, 16, 21})	
			)
		);
	}

}
