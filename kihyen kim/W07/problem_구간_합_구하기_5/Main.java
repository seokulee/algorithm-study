import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		// INIT size, count of test case
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int cntTestCase = Integer.parseInt(st.nextToken());

		// INIT dynamic programming arrays
		int[][] nums = new int[size][size];
		long[][] dpSum = new long[size+1][size+1];
		for (int i = 0; i < size; i++) {
			st = new StringTokenizer(br.readLine());
			
			for (int j = 0; j < size; j++)
			{
				nums[i][j] = Integer.parseInt(st.nextToken());
				dpSum[i+1][j+1] = nums[i][j] + dpSum[i][j+1] + dpSum[i+1][j] - dpSum[i][j];
			}
		}
		
		// CALC test cases
		for (int i = 0; i < cntTestCase; i++) {
			st = new StringTokenizer(br.readLine());
			
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			long result = dpSum[x2][y2] - dpSum[x1-1][y2] - dpSum[x2][y1-1] + dpSum[x1-1][y1-1];
			
			sb.append(result).append("\n");
		}

		// PRINT
		System.out.println(sb);

	}

}