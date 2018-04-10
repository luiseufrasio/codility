package lessons.one.iterations;

/**
 * Let's print a triangle made of asterisks ('*') separated by spaces. The triangl
 * should consist of n rows, where n is a given positive integer, and consecutive rows should
 * contain 1, 2, . . . , n asterisks. For example, for n = 4 the triangle should appear as follows:<pre>
 * *
 * * *
 * * * *
 * * * * *
 * </pre>
 * 
 * @author Luis
 *
 */
public class Example1 {

	public Example1() {
	}

	public static void main(String[] args) {
		
		int N = Integer.parseInt(args[0]);
		
		for (int i = 1; i < N + 1; i++) {
			for (int j = 0; j < i; j++) {
				System.out.print('*');
			}
			System.out.println();
		}
	}

}
