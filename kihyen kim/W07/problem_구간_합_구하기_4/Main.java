import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		// INIT size, count of calculation
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int cntCalc = Integer.parseInt(st.nextToken());

		// INIT numbers, dynamic programming array
		int[] nums = new int[size];
		int[] dpSum = new int[size];
		int sum = 0;
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < size; i++) {
			nums[i] = Integer.parseInt(st.nextToken());

			sum += nums[i];
			dpSum[i] = sum;
		}

		// CALC
		for (int i = 0; i < cntCalc; i++) {
			st = new StringTokenizer(br.readLine());
			int idxStart = Integer.parseInt(st.nextToken()) - 1;
			int idxEnd = Integer.parseInt(st.nextToken()) - 1;
			
			sb.append( dpSum[idxEnd] - (idxStart > 0 ? dpSum[idxStart-1] : 0) ).append("\n");
		}
		
		
		
		// PRINT
		System.out.println(sb);

	}

}