import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, sequence
		int size = Integer.parseInt(br.readLine());
		int[] arrSequence = new int[500];
		String[] splited;
		for (int i = 0; i < size; i++) {
			splited = br.readLine().split(" ");
			
			int idx = Integer.parseInt(splited[0])-1;
			int value = Integer.parseInt(splited[1]);
			arrSequence[idx] = value;
		}
		for (int i=0, j=0; i < 500; i++) { // move empty elements to the end of the array
			if (arrSequence[i] != 0)
				arrSequence[j++] = arrSequence[i];
		}

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
		int result = (size >= 2) ? size - maxDp : 0;
		System.out.println(result);

	}

}