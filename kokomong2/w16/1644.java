
import java.io.*;
import java.util.*;

public class Main {
	static int N, M, res;
	static boolean[] arr;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		arr = new boolean[4000001];
		Arrays.fill(arr, true);
		arr[0] = false;
		arr[1] = false;
		double sqrt = Math.sqrt(N);

		for (int i = 2; i <= sqrt; i++) {
			if (arr[i]) {
				for (int j = 2; i * j <= N; j++) {
					arr[i * j] = false;
				}
			}
		}
		ArrayList<Integer> prime = new ArrayList<>();
		for (int i = 0; i <= 4000000; i++) {
			if (arr[i]){
				prime.add(i);
			}
		}
		int start = 0;
		int sum  = 0;
		int cnt = 0;
		sum += prime.get(0);
		int end = 1;
		int len = prime.size();
		while (end <= N && start <= end) {
			if (sum < N) {
				sum += prime.get(end++);
			} else if (sum > N) {
				sum -= prime.get(start++);
			}else {
				cnt++;
				sum -= prime.get(start++);
			}
			if (start >= len || end >= len)
				break;
		}
		System.out.println(cnt);
	}

}

