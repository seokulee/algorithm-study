import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static long getLcm(long a, long b) {
		if (a < b) {
			long temp = a;
			a = b;
			b = temp;
		}

		long lcm = 0;
		while ((lcm += a) % b != 0)
			;

		return lcm;
	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT numbers
		String[] nums = br.readLine().split(" ");
		long num1 = Long.parseLong(nums[0]);
		long num2 = Long.parseLong(nums[1]);

		// CALC
		long leastCommonMultiple = getLcm(num1, num2);

		// PRINT
		sb.append(leastCommonMultiple);

		System.out.println(sb);

	}

}