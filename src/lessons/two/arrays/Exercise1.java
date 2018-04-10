package lessons.two.arrays;

import java.util.stream.Stream;
import java.util.Arrays;

/**
 * Given array A consisting of N integers, return the reversed array.
 * 
 * @author Luis
 *
 */
public class Exercise1 {

	public Exercise1() {
	}
	
	public int[] reverse(int[] array) {
	    int N = array.length;
	    int[] result = new int[N];
	    
	    for (int i = N; i >= 1; i--) {
	        result[N - i] = array[i - 1];
	    }
	    
	    return result;
	}

	public static void main(String[] args) {

		int[] entry = Stream.of(args).mapToInt(Integer::parseInt).toArray();
		
		int[] result = new Exercise1().reverse(entry);
		
		Arrays.stream(result).forEach(
			(s) -> System.out.print(s + " ")
		);
	}

}