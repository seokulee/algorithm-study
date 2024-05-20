import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, stairs array
		int size = Integer.parseInt(br.readLine());
		int[] arrStairs = new int[size + 1];
		arrStairs[0] = 0; // start floor = 0th stair
		for (int i = 1; i <= size; i++)
			arrStairs[i] = Integer.parseInt(br.readLine());

		// INIT dynamic programming array
		int[] dp = new int[size + 1];
		dp[0] = 0;
		dp[1] = arrStairs[1];
		if (size >= 2) {
			dp[2] = arrStairs[1] + arrStairs[2];
			for (int i = 3; i <= size; i++)
				dp[i] = arrStairs[i] + Math.max(dp[i - 2], dp[i - 3] + arrStairs[i - 1]);
		}

		// PRINT
		System.out.println(dp[size]);

	}

}