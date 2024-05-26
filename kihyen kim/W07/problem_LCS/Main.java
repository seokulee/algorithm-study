import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT two character arrays
		char[] str1 = br.readLine().toCharArray();
		char[] str2 = br.readLine().toCharArray();

		// INIT dynamic programming array
		int[][] dp = new int[str1.length + 1][str2.length + 1]; // row0 & col0 are filled by zero
		for (int i = 0; i < str1.length; i++) {
			for (int j = 0; j < str2.length; j++) {
				if (str1[i] == str2[j])
					dp[i + 1][j + 1] = dp[i][j] + 1;
				else
					dp[i + 1][j + 1] = Math.max(dp[i][j + 1], dp[i + 1][j]);
			}
		}

		// SIMULATOR
		//	StringBuilder sb = new StringBuilder();
		//	sb.append("    ");
		//	for (char c : str2)
		//		sb.append(c).append(" ");
		//	sb.append("\n");
		//
		//	for (int i = 0; i < dp.length; i++) {
		//		sb.append(i == 0 ? "  " : str1[i - 1] + " ");
		//
		//		for (int j = 0; j < dp[i].length; j++)
		//			sb.append(dp[i][j] + " ");
		//
		//		sb.append("\n");
		//	}
		//	System.out.println(sb);

		// PRINT
		System.out.println(dp[str1.length][str2.length]);

	}

}