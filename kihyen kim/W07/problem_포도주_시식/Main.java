import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, Wine array
		int size = Integer.parseInt(br.readLine());
		int[] arrWines = new int[size + 2];
		arrWines[0] = 0;
		for (int i = 1; i <= size; i++)
			arrWines[i] = Integer.parseInt(br.readLine());

		// INIT dynamic programming array
		int[] dp = new int[size + 2];
		dp[0] = 0;
		dp[1] = arrWines[1];
		if (size >= 2) {
			dp[2] = arrWines[1] + arrWines[2];
			for (int i = 3; i <= size + 1; i++)
				if (i == 3)
					dp[i] = arrWines[i] + Math.max(dp[i - 2], dp[i - 3] + arrWines[i - 1]);
				else
					dp[i] = arrWines[i] + Math.max(dp[i - 2], Math.max(dp[i - 3] + arrWines[i - 1], dp[i - 4] + arrWines[i - 1]));
		}

		// PRINT
		int max = Math.max(dp[size], dp[size + 1]);
		System.out.println(max);
		
	}

}