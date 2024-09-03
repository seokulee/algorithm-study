import java.io.*;
import java.util.*;

public class Main {
	static int INF = Integer.MAX_VALUE;
	static int[] costs, pre;
	static ArrayList<Node>[] map;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		StringTokenizer st;
		map = new ArrayList[N + 1];
		for (int i = 0; i <= N; i++) {
			map[i] = new ArrayList<>();
		}
		pre = new int[N + 1];
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			map[a].add(new Node(b, c));
		}
		st = new StringTokenizer(br.readLine());
		int start = Integer.parseInt(st.nextToken());
		int end = Integer.parseInt(st.nextToken());

		boolean[] visited = new boolean[N + 1];
		costs = new int[N + 1];
		Arrays.fill(costs, INF);
		dijkstra(start);
		System.out.println(costs[end]);
		Stack<Integer> stack = new Stack<>();
		stack.push(end);
		int cnt = 0;
		while (pre[end] != 0) {
			cnt++;
			stack.push(pre[end]);
			end = pre[end];
		}
		System.out.println(cnt + 1);
		while (!stack.isEmpty()) {
			System.out.print(stack.pop() + " ");
		}
	}

	private static void dijkstra(int start) {
		PriorityQueue<Node> pq = new PriorityQueue<Node>();
		pq.add(new Node(start, 0));
		costs[start] = 0;

		while (!pq.isEmpty()) {
			Node curCity = pq.poll();
			int cur = curCity.x;
			if (costs[cur] < curCity.cost)
				continue;
			for (Node next : map[cur]) {
				if (costs[next.x] > costs[cur] + next.cost) { // 최단거리 cost 업데이트
					costs[next.x] = costs[cur] + next.cost;
					pre[next.x] = cur; // 이전마을 기록
					pq.offer(new Node(next.x, costs[next.x]));
				}
			}
		}

	}
}

class Node implements Comparable<Node>{
	int x;
	int cost;

	public Node(int x, int cost) {
		this.x = x;
		this.cost = cost;
	}

	@Override
	public int compareTo (Node o) {
		return this.cost - o.cost;
	}
}
