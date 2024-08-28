import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		int start = 0;
		int end = N - 1;
		int min = Integer.MAX_VALUE;
		int minx = 0;
		int miny = N - 1;
		while (start < end) {
			int sum = arr[start] + arr[end];
			if (Math.abs(sum) < Math.abs(min)) {
				min = sum;
				minx = arr[start];
				miny = arr[end];
			}
			if (sum < 0)
				start++;
			else
				end--;
		}
		System.out.println(minx + " " + miny);
	}
}
