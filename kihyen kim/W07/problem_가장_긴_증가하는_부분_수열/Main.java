import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, sequence
		int size = Integer.parseInt(br.readLine());
		int[] arrSequence = new int[size];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < size; i++)
			arrSequence[i] = Integer.parseInt(st.nextToken());

		// INIT dynamic programming array
		int[] dp = new int[size];
		dp[0] = 1;
		int maxDp = 1;
		for (int i = 1; i < size; i++)
		{
			int maxLISBefore = 0;
			for (int j = 0; j < i; j++) {
				if (arrSequence[j] < arrSequence[i])
					maxLISBefore = Math.max(dp[j], maxLISBefore);
			}
			dp[i] = maxLISBefore + 1;

			maxDp = Math.max(dp[i], maxDp);
		}

		// PRINT
		System.out.println(maxDp);

	}

}