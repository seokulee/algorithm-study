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

	static int n, m, t, s, g, h;
	static ArrayList<Node>[] map;
	static long[] cost;
	static boolean[] visited;
	static int INF = Integer.MAX_VALUE;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int j = 0; j < T; j++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());
			int[] sub = new int[t];
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			g = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());
			map = new ArrayList[n + 1];
			for (int i = 0; i <= n; i++) {
				map[i] = new ArrayList<>();
			}
			cost = new long[n + 1];
			visited = new boolean[n + 1];

			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				map[a].add(new Node(b, c));
				map[b].add(new Node(a, c));
			}
			for (int i = 0; i < t; i++) {
				sub[i] = Integer.parseInt(br.readLine());
			}
			PriorityQueue<Integer> pq = new PriorityQueue<>();
			for (int i = 0; i < t; i++) {
				int end = sub[i];
				// g->h
				long len1 = 0;
				len1 += dijkstra(s, g);
				len1 += dijkstra(g, h);
				len1 += dijkstra(h, end);
				// h->g
				long len2 = 0;
				len2 += dijkstra(s, h);
				len2 += dijkstra(h, g);
				len2 += dijkstra(g, end);

				long fullLen = dijkstra(s, end);
				if (fullLen != INF && (fullLen == len1 || fullLen == len2)) {
					pq.add(end);
				}
			}
			while (!pq.isEmpty()) {
				sb.append(pq.poll()).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	public static long dijkstra (int start, int end) {
		Arrays.fill(cost, INF);
		Arrays.fill(visited, false);

		cost[start] = 0;
		
		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(start, 0));
		
		while (!pq.isEmpty()) {
			int now = pq.poll().index;
			if (visited[now])
				continue;
			visited[now] = true;
			for (Node next : map[now]) {
				if (cost[next.index] > cost[now] + next.cost) {
					cost[next.index] = cost[now] + next.cost;
					pq.add(new Node(next.index, cost[next.index]));
				}
			}
		}
		return cost[end];
	}
}

class Node implements Comparable<Node>{
	int index;
	long cost;

	public Node(int index, long cost) {
		this.index = index;
		this.cost = cost;
	}

	@Override
	public int compareTo(Node o) {
		return Long.compare(this.cost, o.cost);
	}
}
