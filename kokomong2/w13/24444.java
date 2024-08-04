
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static ArrayList<Integer>[] map;
	static int[] cntArr;
	static boolean[] visited;
	static int N, M, R, cnt = 1;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		R = Integer.parseInt(st.nextToken());

		map = new ArrayList[N + 1];
		for (int i = 1; i <= N; i++) {
			map[i] = new ArrayList<>();
		}
		visited = new boolean[N + 1];
		cntArr = new int[N + 1];

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());

			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());

			map[u].add(v);
			map[v].add(u);
		}
		visited[R] = true;
		Queue<Integer> q = new LinkedList<>();
		q.add(R);
		while (!q.isEmpty()) {
			int now = q.poll();
			cntArr[now] = cnt++;
			Collections.sort(map[now]);
			for (int i : map[now]) {
				if (!visited[i]) {
					visited[i] = true;
					q.add(i);
				}
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= N; i++) {
			sb.append(cntArr[i]).append("\n");
		}
		System.out.println(sb);
	}

	// bfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
	// 	for each v ∈ V - {R}
	// 		visited[v] <- NO;
	// 	visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
	// 	enqueue(Q, R);  # 큐 맨 뒤에 시작 정점 R을 추가한다.
	// 	while (Q ≠ ∅) {
	// 		u <- dequeue(Q);  # 큐 맨 앞쪽의 요소를 삭제한다.
	// 		for each v ∈ E(u)  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
	// 		if (visited[v] = NO) then {
	// 			visited[v] <- YES;  # 정점 v를 방문 했다고 표시한다.
	// 				enqueue(Q, v);  # 큐 맨 뒤에 정점 v를 추가한다.
	// 		}
	// 	}
	// }
}
