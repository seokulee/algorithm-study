import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		br.readLine(); // skip size
		StringTokenizer st = new StringTokenizer(br.readLine());
		while (st.hasMoreTokens()) {
			int num = Integer.parseInt(st.nextToken());
			max = (max < num) ? num : max;
			min = (min > num) ? num : min;
		}

		// PRINT
		System.out.println(max * min);

	}

}