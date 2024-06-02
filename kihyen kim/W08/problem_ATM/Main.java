import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, array of duration
		int size = Integer.parseInt(br.readLine());
		int[] arrDurations = new int[size];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < size; i++)
			arrDurations[i] = Integer.parseInt(st.nextToken());
		Arrays.sort(arrDurations);

		// CALC
		int result = 0;
		int multiple = size;
		for (int duration : arrDurations)
			result += duration * multiple--;
		
		// PRINT
		System.out.println(result);

	}

}