package lessons.one.iterations;

/**
 * The Fibonacci numbers4 form a sequence of integers defined recursively in the
 * following way. The first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent
 * number is the sum of the previous two. The first few elements in this sequence are: 0,
 * 1, 1, 2, 3, 5, 8, 13. Let�s write a program that prints all the Fibonacci numbers, not exceeding
 * a given integer n.
 * 
 * @author Luis
 */
public class Example4 {

	public Example4() {
	}

	public static void main(String[] args) {
		int N = Integer.parseInt(args[0]);
		int i = 0;
		int j = 1;
		while (i <= N) {
			System.out.print(i + " ");
			int k = j;
			j += i;
			i = k;
		}
	}

}
