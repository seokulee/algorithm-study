import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		// INIT size, test cases
		int size = Integer.parseInt(br.readLine());
		int[] arrTC = new int[size];
		int max = 0;
		for (int i=0; i<size; i++) {
			arrTC[i] = Integer.parseInt(br.readLine());
			max = (max < arrTC[i]) ? arrTC[i] : max;
		}

		// INIT dynamic programming array
		long[] dp = new long[100];
		dp[0] = 1;
		dp[1] = 1;
		dp[2] = 1;
		dp[3] = 2;
		dp[4] = 2;
		for (int i=5; i<max; i++)
			dp[i] = (dp[i-5] + dp[i-1]);

		// PRINT
		for (int tc : arrTC)
			sb.append(dp[tc-1]).append("\n");
		System.out.println(sb);
		
	}

}