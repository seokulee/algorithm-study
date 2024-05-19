import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size
		int size = Integer.parseInt(br.readLine());

		// CALC by dynamic programming array
		int[] dp = new int[(size < 2) ? 2 : size];
		dp[0] = 1;
		dp[1] = 2;
		for (int i = 2; i < size; i++) {
			dp[i] = (dp[i - 1] + dp[i - 2]) % 15746;
		}

		// PRINT
		System.out.println(dp[size - 1]);

	}

}