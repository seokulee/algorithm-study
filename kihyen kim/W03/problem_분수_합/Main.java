import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static int getGcd(int a, int b) {
		int euclidean = (a > b) ? a : b;
		int divisor = (a > b) ? b : a;

		while (divisor != 0) {
			int temp = divisor;
			divisor = euclidean % divisor;
			euclidean = temp;
		}

		return euclidean;
	}

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT fractions
		int[] fraction1 = new int[2];
		int[] fraction2 = new int[2];
		String[] nums;
		nums = br.readLine().split(" ");
		fraction1[0] = Integer.parseInt(nums[0]);
		fraction1[1] = Integer.parseInt(nums[1]);
		nums = br.readLine().split(" ");
		fraction2[0] = Integer.parseInt(nums[0]);
		fraction2[1] = Integer.parseInt(nums[1]);

		// CALC addition of fractions
		int[] fractionAdded = new int[2];
		fractionAdded[0] = (fraction1[0] * fraction2[1]) + (fraction2[0] * fraction1[1]);
		fractionAdded[1] = fraction1[1] * fraction2[1];

		// CALC irreducible fraction of result fraction
		int gcd = getGcd(fractionAdded[0], fractionAdded[1]);
		fractionAdded[0] /= gcd;
		fractionAdded[1] /= gcd;

		// PRINT
		sb.append(fractionAdded[0]).append(" ").append(fractionAdded[1]);
		System.out.println(sb);

	}

}