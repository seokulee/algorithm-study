import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, count of calculation
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int total = Integer.parseInt(st.nextToken());

		// INIT coins
		int[] coins = new int[size];
		for (int i=size-1; i>=0; i--)
			coins[i] = Integer.parseInt(br.readLine());

		// CALC
		int result = 0;
		for (int i=0; total != 0; i++) {
			result += total / coins[i];
			total = total % coins[i];
		}
		
		// PRINT
		System.out.println(result);

	}

}