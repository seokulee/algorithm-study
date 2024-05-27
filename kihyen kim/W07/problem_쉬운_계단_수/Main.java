import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size
		int size = Integer.parseInt(br.readLine());

		// INIT dynamic programming array
		/* examples
		 * [lastNum]	0 1 2 3 4 5 6 7 8 9
		 * if len==1	0 1 1 1 1 1 1 1 1 1	['1','2','3' ... 9]
		 * if len==2	1 1 2 2 2 2 2 2 2 1	[1'0',2'1',1'2',3'2',2'3',4'3' ... 8'9']
		 * if len==3	1 3 3 4 4 4 4 4 3 2	[21'0',10'1',12'1',32'1' ...]
		 * */
		long[][] dp = new long[size][10];
		for (int i = 1; i <= 9; i++)
			dp[0][i] = 1;

		for (int i = 1; i < size; i++) {
			for (int j = 1; j <= 8; j++)
				dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000;
			
			dp[i][0] = dp[i - 1][1] % 1000000000; // ###0 => nearest num must 1, first blank must not 0
			dp[i][9] = dp[i - 1][8] % 1000000000; // ###9 => nearest num must 8
		}

		// PRINT
		long sum = 0;
		for (long value : dp[size-1])
			sum += value;
		System.out.println(sum % 1000000000);

	}

}