import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT numN, numK
		String[] nums = br.readLine().split(" ");
		int numN = Integer.parseInt(nums[0]);
		int numK = Integer.parseInt(nums[1]);

		// CALC binomial coefficient
		Function<Integer, Integer> factorial = n ->
		{
			int result = 1;
			while (n > 1)
				result *= n--;
			return result;
		};
		int result = factorial.apply(numN) / (factorial.apply(numK) * factorial.apply(numN - numK));

		// PRINT
		System.out.println(result);

	}

}