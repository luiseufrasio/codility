package lessons.one.iterations;

/**
 * Given a positive integer n, how can we count the number of digits in its decimal
 * representation? One way to do it is convert the integer into a string and count the characters.
 * Here, though, we will use only arithmetical operations instead. We can simply keep dividing
 * the number by ten and count how many steps are needed to obtain 0.
 * 
 * @author Luis
 */
public class Example3 {

	public Example3() {
	}

	public static void main(String[] args) {
		int N = Integer.parseInt(args[0]);
		int result = 0;
		
		while (N > 0) {
			N /= 10;
			result++;
		}
		
		System.out.println(result);
	}

}