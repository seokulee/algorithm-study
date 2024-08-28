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
		int X = Integer.parseInt(br.readLine());
		int start = 0;
		int end = N - 1;
		int cnt = 0;
		while (start < end) {
			int sum = arr[start] + arr[end];
			if (sum == X) {
				cnt++;
				start++;
				end--;
			} else if (sum < X) {
				start++;
			} else {
				end--;
			}
		}
		System.out.println(cnt);
	}
}
