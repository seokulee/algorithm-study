import java.io.*;
import java.util.*;

public class Main {

	static int[][] dp;
	static int[] weight;
	static boolean[] visited;
	static List<Integer>[] edges;
	static StringBuilder sb = new StringBuilder();
	static List<Integer> list = new ArrayList<>();
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		weight = new int[n + 1];
		visited = new boolean[n + 1];
		dp = new int[n + 1][2];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= n; i++) {
			weight[i] = Integer.parseInt(st.nextToken());
		}

		edges = new ArrayList[n + 1];

		for (int i = 0; i <= n; i++) {
			edges[i] = new ArrayList<>();
		}

		for (int i = 0; i < n - 1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			edges[a].add(b);
			edges[b].add(a);
		}

		dfs(1);
		sb.append(Math.max(dp[1][0], dp[1][1])).append("\n");
		Arrays.fill(visited, false);

		if (dp[1][1] > dp[1][0])
			trace(1,1);
		else
			trace(1, 0);

		Collections.sort(list);
		for(int i : list) {
			sb.append(i).append(" ");
		}
		System.out.println(sb);
	}

	public static void dfs (int now) {
		visited[now] = true;

		dp[now][1] = weight[now];

		for (int next : edges[now]) {
			if (visited[next])
				continue;
			dfs(next);
			// 내가 포함 안될때
			if (dp[next][0] > dp[next][1])
				dp[now][0] += dp[next][0];
			else
				dp[now][0] += dp[next][1];

			// 내가 포함되고 자식은 포함 안될때
			dp[now][1] += dp[next][0];
		}
	}

	public static void trace (int now, int attend){
		visited[now] = true;
		if (attend == 1)
			list.add(now);
		for (int next : edges[now]) {
			if (visited[next])
				continue;
			if (attend == 1) {
				trace(next, 0);
			}else {
				if (dp[next][0] > dp[next][1])
					trace(next, 0);
				else
					trace(next, 1);
			}
		}
	}
}
