import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, divisor
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int divisor = Integer.parseInt(st.nextToken());

		// INIT dynamic programming arrays
		int[] nums = new int[size];
		long[] dpSum = new long[size];
		long[] dpRemainder = new long[divisor]; // dpRemainder[1] : counts of remainder of 1 when divided
		long sum = 0;
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < size; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
			sum += nums[i];

			dpSum[i] = sum;
			dpRemainder[(int) (dpSum[i] % divisor)]++;
		}

		// CALC
		long result = 0 + dpRemainder[0]; // firstly, add to divisible things
		for (int i = 0; i < divisor; i++)
			result += dpRemainder[i] * (dpRemainder[i] - 1) / 2; // add to (x C 2) things

		// PRINT
		System.out.println(result);

	}

}