
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		Map<Integer, Integer> ladderMap = new HashMap<>();
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			ladderMap.put(start, end);
		}
		Map<Integer, Integer> snakeMap = new HashMap<>();
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			snakeMap.put(start, end);
		}

		boolean[] visited = new boolean[101];
		visited[0] = true;
		visited[1] = true;
		PriorityQueue<Pair> pq = new PriorityQueue();
		pq.add(new Pair(1, 0));
		int res = 0;
		while(!pq.isEmpty()) {
			Pair pair = pq.poll();
			if (pair.x == 100) {
				res = pair.cnt;
				break;
			}
			for (int i = 1; i <= 6; i++) {
				int nx = pair.x + i;
				if (nx > 100 || visited[nx])
					continue;
				if (ladderMap.containsKey(nx))
					nx = ladderMap.get(nx);
				else if (snakeMap.containsKey(nx))
					nx = snakeMap.get(nx);
				visited[nx] = true;
				pq.add(new Pair(nx, pair.cnt + 1));
			}
		}
		System.out.println(res);
 	}
}

class Pair implements Comparable<Pair>{
	int x;
	int cnt;

	public Pair(int x, int cnt) {
		this.x = x;
		this.cnt = cnt;
	}

	@Override
	public int compareTo(Pair o) {
		if (this.cnt == o.cnt) {
			return this.x - o.x;
		}
		return this.cnt - o.cnt;
	}
}
