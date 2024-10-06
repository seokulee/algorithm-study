import java.io.*;
import java.util.*;

public class Main {
	static int N, M;
	static int[] parent;

	public static int find(int x) {
		if (x == parent[x]) {
			return x;
		}
		return parent[x] = find(parent[x]);
	}
	public static void union(int x, int y) {
		x = find(x);
		y = find(y);
		if (x != y) {
			if (x < y) {
				parent[y] = x;
			} else {
				parent[x] = y;
			}
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());

		parent = new int[N+1];

		for (int i=0; i<N+1; i++) parent[i] = i;

		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int a = Integer.parseInt(st.nextToken());
				if (a == 1) {
					union(i + 1, j + 1);
				}
			}
		}
		st = new StringTokenizer(br.readLine());
		int parent = find(Integer.parseInt(st.nextToken()));
		boolean isTrue = true;
		for (int i = 1; i < M; i++) {
			int a = find(Integer.parseInt(st.nextToken()));
			if (parent != a)
				isTrue = false;
		}
		if (isTrue)
			System.out.println("YES");
		else
			System.out.println("NO");
	}
}
