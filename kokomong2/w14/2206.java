

import java.io.*;
import java.util.*;

public class Main {
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[][] map = new int[N][M];
		int[][] visited = new int[N][M];
		for (int i = 0; i < N; i++) {
			String input = br.readLine();
			for (int j = 0; j < M; j++) {
				map[i][j] = input.charAt(j) - '0';
			}
		}
		if (N == 1 && M == 1) {
			System.out.println("1");
			return ;
		}

		PriorityQueue<Pair> q = new PriorityQueue<>();
		q.add(new Pair(0, 0, false, 0));
		visited[0][0] = 1;
		int cnt = 0;
		while (!q.isEmpty()) {
			Pair pair = q.poll();
			if (pair.y == N - 1 && pair.x == M - 1) {
				cnt = pair.cnt;
				break;
			}
			for (int i = 0; i < 4; i++) {
				int nx = pair.x + dx[i];
				int ny = pair.y + dy[i];
				if (nx >= 0 && ny >= 0 && nx < M && ny < N && visited[ny][nx] == 0) {
					if (map[ny][nx] == 1) {
						if (!pair.isBreak) {
							visited[ny][nx] = 1;
							q.add(new Pair(nx, ny, true, pair.cnt + 1));
						}
					} else {
						visited[ny][nx] = 1;
						q.add(new Pair(nx, ny, pair.isBreak, pair.cnt + 1));
					}
				}
			}

		}
		q = new PriorityQueue<>();
		visited = new int[N][M];
		visited[N - 1][M - 1] = 1;
		q.add(new Pair(M - 1, N - 1, false, 0));
		while (!q.isEmpty()) {
			Pair pair = q.poll();
			if (pair.y == 0 && pair.x == 0) {
				if (cnt == 0) {
					cnt = pair.cnt;
				} else {
					cnt = Math.min(cnt, pair.cnt);
				}
				break;
			}
			for (int i = 0; i < 4; i++) {
				int nx = pair.x + dx[i];
				int ny = pair.y + dy[i];
				if (nx >= 0 && ny >= 0 && nx < M && ny < N && visited[ny][nx] == 0) {
					if (map[ny][nx] == 1) {
						if (!pair.isBreak) {
							visited[ny][nx] = 1;
							q.add(new Pair(nx, ny, true, pair.cnt + 1));
						}
					} else {
						visited[ny][nx] = 1;
						q.add(new Pair(nx, ny, pair.isBreak, pair.cnt + 1));
					}
				}
			}
		}
		if (cnt == 0) {
			System.out.println("-1");
		} else {
			System.out.println(cnt + 1);
		}
	}
}

class Pair implements Comparable<Pair>{
	int x;
	int y;

	boolean isBreak;
	int cnt;

	public Pair(int x, int y, boolean isBreak, int cnt) {
		this.x = x;
		this.y = y;
		this.isBreak = isBreak;
		this.cnt = cnt;
	}

	@Override
	public int compareTo(Pair o) {
		if (this.cnt < o.cnt)
			return -1;
		else if (this.cnt == o.cnt) {
			if (!this.isBreak && o.isBreak) {
				return -1;
			} else if (this.isBreak && !o.isBreak) {
				return 1;
			} else {
				return 0;
			}
		}
		return 1;
	}
}
