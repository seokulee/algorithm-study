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
		dfs(R);
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= N; i++) {
			sb.append(cntArr[i]).append("\n");
		}
		System.out.println(sb);
	}

	// 문제의 dfs
    // dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    //     visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    //     for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 내림차순으로 방문한다)
    //     if (visited[x] = NO) then dfs(V, E, x);
    // }
	static void dfs(int R) {
		cntArr[R] = cnt;
		visited[R] = true;
		map[R].sort(Collections.reverseOrder());
		for (int i : map[R]) {
			if (!visited[i]) {
				cnt++;
				dfs(i);
			}
		}
	}
}
