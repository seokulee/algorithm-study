import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT number
		int num = Integer.parseInt(br.readLine());

		// INIT dynamic programming array
		int[] dp = new int[1000001];
		dp[1] = 0;
		dp[2] = 1;
		dp[3] = 1;
		for (int i = 4; i <= num; i++) {
			if (i % 6 == 0)
				dp[i] = Math.min(dp[i / 3], Math.min(dp[i / 2], dp[i - 1])) + 1;
			else
			if (i % 3 == 0)
				dp[i] = Math.min(dp[i / 3], dp[i - 1]) + 1;
			else
			if (i % 2 == 0)
				dp[i] = Math.min(dp[i / 2], dp[i - 1]) + 1;
			else
				dp[i] = dp[i - 1] + 1;
			
			// System.out.println("dp[" + i + "] : " + dp[i]);
		}

		// PRINT
		System.out.println(dp[num]);

	}

}