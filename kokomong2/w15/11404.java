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
		StringTokenizer st;
		N = Integer.parseInt(br.readLine());
		M = Integer.parseInt(br.readLine());

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

		long[][] res = new long[N][N];

		for (int i = 1; i <= N; i++) {
			dijkstra(i);
			for (int j = 1; j <= N; j++) {
				if (i == j)
					continue;
				if (cost[j] != Integer.MAX_VALUE)
					res[i - 1][j - 1] = cost[j];
				else
					res[i - 1][j - 1] = 0;
			}
		}

		StringBuilder sb = new StringBuilder();

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {

				sb.append(res[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb);
	}

	public static void dijkstra (int start) {
		Arrays.fill(cost, INF);
		Arrays.fill(visited, false);
		cost[start] = 0;

		PriorityQueue<Node> pq = new PriorityQueue<>();
		pq.add(new Node(start, 0));

		while (!pq.isEmpty()) {
			Node now = pq.poll();
			if (visited[now.index])
				continue;
			visited[now.index] = true;
			for (Node next : map[now.index]) {
				if (cost[next.index] > cost[now.index] + next.cost) {
					cost[next.index] = cost[now.index] + next.cost;

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
