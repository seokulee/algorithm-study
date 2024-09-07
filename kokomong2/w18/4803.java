import java.io.*;
import java.util.*;

public class Main {
	static int[] parent;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int caseNum = 1;
		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			if (n == 0 && m == 0)
				break;
			parent = new int[n + 1];
			for (int i = 1; i <= n; i++) {
				parent[i] = i;
			}
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				unionParent(a, b);
			}
			Set<Integer> set = new HashSet<>();
			for (int i = 1; i <= n; i++) {
				int now = getParent(i);
				if (now > 0)
					set.add(now);
			}
			int T = set.size();
			sb.append("Case ").append(caseNum);
			if (T == 0)
				sb.append(": No trees.");
			else if (T == 1)
				sb.append(": There is one tree.");
			else
				sb.append(": A forest of ").append(T).append(" trees.");
			sb.append("\n");
			caseNum++;
		}
		System.out.println(sb);
	}

	public static void unionParent(int a, int b) {
		a = getParent(a);
		b = getParent(b);
		if (b < a) {
			int tmp = b;
			b = a;
			a = tmp;
		}
		if (a == b)
			parent[a] = 0;
		else
			parent[b] = a;
	}

	public static int getParent (int a) {
		if (parent[a] == a) return a;
		return parent[a] = getParent(parent[a]);
	}

}
