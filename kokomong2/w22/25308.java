import java.io.*;
import java.util.*;

public class Main {
	static int[] arr, origin;
	static int sum = 0;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		arr = new int[8];
		origin = new int[8];
		for (int i = 0; i < 8; i++) {
			origin[i] = Integer.parseInt(st.nextToken());
		}

		cor(0, new boolean[8]);
		System.out.println(sum);
	}

	public static boolean check (int index) {

		int pre = (index == 0 ? arr[7] : arr[index - 1]);
		int next = (index == 7 ? arr[0] : arr[index + 1]);
		double line = Math.sqrt(2) * (origin[pre] * origin[next])/(origin[pre] + origin[next]);
		return origin[arr[index]] > line;
	}

	public static void cor (int d,  boolean[] visited) {
		if (d == 8) {
			boolean isTrue = true;
			for (int i = 0; i < 8; i++) {
				if (!check(i))
					isTrue = false;
			}
			if (isTrue)
				sum++;
			return;
		}
		for (int i = 0; i < 8; i++) {
			if (!visited[i]) {
				arr[d] = i;
				visited[i] = true;
				cor(d + 1, visited);
				visited[i] = false;
			}
		}
	}
}

