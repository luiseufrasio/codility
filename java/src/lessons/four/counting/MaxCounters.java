package lessons.four.counting;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * <pre>You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

class Solution { public int[] solution(int N, int[] A); }

that, given an integer N and a non-empty zero-indexed array A consisting of M integers, returns a sequence of integers representing the values of the counters.

The sequence should be returned as:

a structure Results (in C), or
a vector of integers (in C++), or
a record Results (in Pascal), or
an array of integers (in any other programming language).
For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Assume that:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).</pre>
 * 
 * @author 49770413
 * @see <a href='https://app.codility.com/demo/results/trainingEY5QW4-PYC/'>Results</a>
 */
public class MaxCounters {
	public int[] solution(int N, int[] A) {
		System.out.println(N);
		System.out.println(Arrays.toString(A));
		
		int M = A.length;
		int MAX = 0;
		int MIN = -1;
		int iMAX = -1;
		int ultMAX = 0;
		
		Map<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < M; i++) {
			int j = A[i];

			if (j > N) {
				iMAX = i;
				ultMAX = MAX;
				MIN = MAX;
			} else {
				Integer e = map.get(j);
				if (e == null) {
					e = 1;
				} else {
					e++;
				}
				
				if (MIN > -1 && e <= MIN) {
					e = MIN;
					e++;
				}
				
				map.put(j, e);
				
				if (e > MAX) {
					MAX = e;
				}
			}
		}

		int[] counters = new int[N];
		for (int i = 0; i < N; i++) {
			counters[i] = ultMAX;
		}
		
		for (int i = iMAX + 1; i < M; i++) {
			int j = A[i] - 1;
			counters[j]++;
		}
		
		return counters;
	}
}
