
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static boolean[] visited;
	static int[] cost;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		cost = new int[200000];
		Arrays.fill(cost, -1);
		cost[N] = 0;
		PriorityQueue<Node> pq = new PriorityQueue<>();
		visited = new boolean[200000];
		pq.add(new Node(N, 0));
		if (N < K){
			while (!pq.isEmpty()) {
				Node now = pq.poll();
				int i = now.x ;
				if (visited[i])
					continue;
				visited[i] = true;
				if (i < K * 2 - 1) {
					if (cost[i + 1] == -1)
						cost[i + 1] = cost[i] + 1;
					else
						cost[i + 1] = Math.min(cost[i] + 1, cost[i + 1]);
					pq.add(new Node(i + 1, cost[i + 1]));
				}
				if (i > 0) {
					if (cost[i - 1] == -1)
						cost[i - 1] = cost[i] + 1;
					else
						cost[i - 1] = Math.min(cost[i] + 1, cost[i - 1]);
					pq.add(new Node(i - 1, cost[i - 1]));
				}
 				if (i < K) {
					if (cost[i * 2] == -1)
						cost[i * 2] = cost[i];
					else
						cost[i * 2] = Math.min(cost[i * 2], cost[i]);
					pq.add(new Node(i * 2, cost[i * 2]));
				}
			}
			System.out.println(cost[K]);
		} else if (N > K) {
			System.out.println(N - K);
		} else {
			System.out.println("0");
		}
	}
}

class Node implements Comparable<Node> {
	int x;
	int cost;

	public Node(int x, int cost) {
		this.x = x;
		this.cost = cost;
	}

	@Override
	public int compareTo(Node o) {
		return this.cost - o.cost;
	}
}

