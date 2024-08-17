
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static boolean[] visited;
	static int[] cost;
	static ArrayList<Pair>[] map;
	static int INF = 2000000000;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());

		map = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			map[i] = new ArrayList<>();
		}
		for (int i = 0; i < E; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			map[a].add(new Pair(b, c));
			map[b].add(new Pair(a, c));
		}
		st = new StringTokenizer(br.readLine());
		int v1 = Integer.parseInt(st.nextToken());
		int v2 = Integer.parseInt(st.nextToken());
		visited = new boolean[N + 1];
		cost = new int[N + 1];
		visited[0] = true;

		// 1 -> v1 -> v2 -> N
		long res1 = 0;
		res1 += dijkstra(1, v1);
		res1 += dijkstra(v1, v2);
		res1 += dijkstra(v2, N);

		// 1 -> v2 -> v1 -> N
		long res2 = 0;
		res2 += dijkstra(1, v2);
		res2 += dijkstra(v2, v1);
		res2 += dijkstra(v1, N);

		long res;
		if (res1 >= INF && res2 >= INF)
			res = -1;
		else
			res = Math.min(res1, res2);

		System.out.println(res);
 	}

	 private static int dijkstra (int start, int end) {
		PriorityQueue<Pair> pq = new PriorityQueue<>();
		pq.add(new Pair(start, 0));
		Arrays.fill(visited, false);
		Arrays.fill(cost, INF);

		cost[start] = 0;

		while (!pq.isEmpty()) {
			Pair now = pq.poll();

			if (visited[now.x])
				continue;
			visited[now.x] = true;
			for (Pair next : map[now.x]) {
				if (cost[next.x] > next.length + now.length) {
					cost[next.x] = next.length + now.length;
					pq.add(new Pair(next.x, cost[next.x]));
				}
			}
		}
		return cost[end];
	 }
}

class Pair implements Comparable<Pair>{
	int x;
	int length;
	public Pair(int x, int length) {
		this.x = x;
		this.length = length;
	}

	@Override
	public int compareTo(Pair o) {
		return this.length - o.length;
	}
}
