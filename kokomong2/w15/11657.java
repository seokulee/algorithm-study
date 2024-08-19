import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

class City {
	int end;
	int weight;

	City(int end, int weight) {
		this.end = end;
		this.weight = weight;
	}
}

public class Main {
	static int N, M;
	static ArrayList<ArrayList<City>> a;
	static long[] dist;
	static final int INF = 987654321;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());

		a = new ArrayList<>();
		dist = new long[N + 1];

		for (int i = 0; i <= N; i++) {
			a.add(new ArrayList<>());
			dist[i] = INF;
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());

			a.get(A).add(new City(B, C));
		}

		StringBuilder sb = new StringBuilder();
		if (bellmanFord()) {
			sb.append("-1\n");
		} else {
			for (int i = 2; i <= N; i++) {
				if (dist[i] == INF) {
					sb.append("-1\n");
				} else {
					sb.append(dist[i] + "\n");
				}
			}
		}

		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	public static boolean bellmanFord() {
		dist[1] = 0;
		boolean update = false;

		for (int i = 1; i < N; i++) {
			update = false;

			for (int j = 1; j <= N; j++) {
				for (City city : a.get(j)) {
					if (dist[j] == INF) {
						break;
					}

					if (dist[city.end] > dist[j] + city.weight) {
						dist[city.end] = dist[j] + city.weight;
						update = true;
					}
				}
			}

			if (!update) {
				break;
			}
		}
		
		if (update) {
			for (int i = 1; i <= N; i++) {
				for (City city : a.get(i)) {
					if (dist[i] == INF) {
						break;
					}

					if (dist[city.end] > dist[i] + city.weight) {
						return true;
					}
				}
			}
		}

		return false;
	}

}