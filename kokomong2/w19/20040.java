import java.io.*;
import java.util.*;

public class Main {
	static int N, M, cnt, res;
	static int[] parent;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st= new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		parent = new int[N];

		for (int i = 0; i < N; i++) parent[i] = i;
		cnt = 1;
		res = 0;
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			union(a, b);
			if (res != 0)
				break;
			cnt++;
		}
		System.out.println(res);
	}

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
		} else {
			res = cnt;
		}
	}
}
