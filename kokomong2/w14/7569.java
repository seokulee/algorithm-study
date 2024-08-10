
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	static int[] dx = {1, -1, 0, 0, 0, 0};
	static int[] dy = {0, 0, 1, -1, 0, 0};
	static int[] dz = {0, 0, 0, 0, 1, -1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		int H = Integer.parseInt(st.nextToken());
		int[][][] map = new int[H][N][M];

		Queue<Pair> q = new LinkedList<>();
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < N; j++) {
				st = new StringTokenizer(br.readLine());
				for (int k = 0; k < M; k++) {
					map[i][j][k] = Integer.parseInt(st.nextToken());
					if (map[i][j][k] == 1)
						q.add(new Pair(k, j, i, 1));
				}
			}
		}
		int max = 0;
		while (!q.isEmpty()) {
			Pair pair = q.poll();
			for (int i = 0; i < 6; i++) {
				int nz = pair.z + dz[i];
				int nx = pair.x + dx[i];
				int ny = pair.y + dy[i];
				if (nz >= 0 && nz < H && nx >= 0 && ny >= 0 && nx < M && ny < N && map[nz][ny][nx] == 0) {
					max = Math.max(max, pair.cnt);
					map[nz][ny][nx] = pair.cnt;
					q.add(new Pair(nx, ny, nz, pair.cnt + 1));
				}
			}
		}
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < N; j++) {
				for (int k = 0; k < M; k++) {
					if (map[i][j][k] == 0) {
						max = -1;
						break;
					}
				}
			}
		}
		System.out.println(max);
	}
}

class Pair {
	int x;
	int y;
	int z;
	int cnt;

	public Pair(int x, int y, int z, int cnt) {
		this.x = x;
		this.y = y;
		this.z = z;
		this.cnt = cnt;
	}
}
