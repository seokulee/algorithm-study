import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, length of calculation
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int lenCalc = Integer.parseInt(st.nextToken());

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
		int max = Integer.MIN_VALUE;
		for (int i = lenCalc-1; i < size; i++) {
			int unincluded = (i-lenCalc < 0 ? 0 : dpSum[i-lenCalc]);
			max = Math.max(max, dpSum[i] - unincluded);
		}
		
		// PRINT
		System.out.println(max);

	}

}