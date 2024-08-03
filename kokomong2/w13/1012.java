
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int M = Integer.parseInt(st.nextToken());
			int N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());

			int[][] map = new int[N][M];
			boolean[][] visited = new boolean[N][M];
			for (int j = 0; j < K; j++) {
				st = new StringTokenizer(br.readLine());
				int X = Integer.parseInt(st.nextToken());
				int Y = Integer.parseInt(st.nextToken());
				map[Y][X] = 1;
			}
			int cnt = 0;

			for (int j = 0; j < M; j++) {
				for (int k = 0; k < N; k++) {
					if (map[k][j] == 1 && !visited[k][j]) {
						cnt++;
						Queue<Pair> q = new LinkedList<>();
						visited[k][j] = true;
						q.add(new Pair(j, k));
						while (!q.isEmpty()) {
							Pair pair = q.poll();
							for (int l = 0; l < 4; l++) {
								int nx = pair.x + dx[l];
								int ny = pair.y + dy[l];
								if (ny >= 0 && nx >= 0 && nx < M && ny < N && !visited[ny][nx] && map[ny][nx] == 1) {
									visited[ny][nx] = true;
									q.add(new Pair(nx, ny));
								}
							}
						}
					}
				}
			}
			System.out.println(cnt);
		}
	}
}

class Pair {
	int x;
	int y;

	public Pair(int x, int y) {
		this.x = x;
		this.y = y;
	}
}
