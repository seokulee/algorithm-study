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

	static int N, M;
	static ArrayList<Node>[] map;
	static long[] cost;
	static boolean[] visited;
	static int INF = Integer.MAX_VALUE;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		map = new ArrayList[N + 1];
		for (int i = 0; i <= N; i++) {
			map[i] = new ArrayList<>();
		}
		cost = new long[N + 1];
		visited = new boolean[N + 1];

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			map[a].add(new Node(b, c));
		}
		long min = INF;
		for (int i = 1; i <= N; i++) {
			dijkstra(i);
			if (cost[i] != 0)
				min = Math.min(min, cost[i]);
		}
		if (min == INF)
			min = -1;
		System.out.println(min);
	}

	public static void dijkstra (int start) {
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
				if (cost[next.index] == 0)
					cost[next.index] = INF;
				if (cost[next.index] > cost[now] + next.cost) {
					cost[next.index] = cost[now] + next.cost;
					pq.add(new Node(next.index, cost[next.index]));
				}
			}
		}
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
