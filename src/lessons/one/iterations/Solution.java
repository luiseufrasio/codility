package lessons.one.iterations;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {

	public Solution() {
	}
	
	public int solution(int N) {
		String binaryN = Integer.toBinaryString(N);
		int result = 0;
		
		Pattern pattern = Pattern.compile("1(0)+1");
		Matcher matcher = pattern.matcher(binaryN);
		int start = 0;
		while (matcher.find(start))
		{
		    int numberZeros = matcher.group().length() - 2;
		    result = numberZeros > result ? numberZeros : result;
		    
		    start = matcher.end() - 1;
		}

		return result;
	}

}
