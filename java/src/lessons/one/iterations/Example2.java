package lessons.one.iterations;

/**
 * Let's print a triangle made of asterisks ('*') separated by spaces and consisting
 * of n rows again, but this time upside down, and make it symmetrical. Consecutive rows should
 * contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
 * spaces. For example, for n = 4 the triangle should appear as follows:<pre>
 *  * * * * * * *
 *    * * * * *
 *      * * *
 *        *
 * </pre>
 * @author Luis
 */
public class Example2 {

	public Example2() {
	}

	public static void main(String[] args) {
		
		int N = Integer.parseInt(args[0]);
		for (int i = N; i > 0; i--) {
			
			for (int j = 0; j < N - i; j++) {
				System.out.print(' ');
			}
			for (int k = 0; k < (2 * i) - 1; k++) {
				System.out.print('*');
			}
			
			System.out.println();
		}
	}

}