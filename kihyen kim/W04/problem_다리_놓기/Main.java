import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size
		int size = Integer.parseInt(br.readLine());

		// CALC by dynamic programming array
		//	int[][] arrDP = new int[30][30];
		//	{
		//		for (int i = 0; i < 30; i++) {
		//			arrDP[i][i] = 1; // 1 1, 2 2, 3 3 ...
		//			arrDP[i][0] = 1;
		//		}
		//	
		//		// numN, numM (0 < numN ≤ numM < 30)
		//		for (int m = 1; m < 30; m++)
		//			for (int n = 1; n <= m; n++)
		//				arrDP[m][n] = arrDP[m - 1][n - 1] + arrDP[m - 1][n];
		//	}
		//	for (int i = 0; i < size; i++) {
		//		String[] nums = br.readLine().split(" ");
		//		int numN = Integer.parseInt(nums[0]);
		//		int numM = Integer.parseInt(nums[1]);
		//	
		//	    sb.append(arrDP[numM][numN]).append('\n');
		//	}
		// CALC normal
		for (int i = 0; i < size; i++) {
			String[] nums = br.readLine().split(" ");
			int numN = Integer.parseInt(nums[0]);
			int numM = Integer.parseInt(nums[1]);

			int result = 1;
			for (int j = 0; j < numN; j++) {
				result *= numM - j;
				result /= j + 1;
			}

			sb.append(result).append('\n');
		}

		// PRINT
		System.out.println(sb);

	}

}