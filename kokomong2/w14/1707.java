import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int V = Integer.parseInt(st.nextToken());
			int E = Integer.parseInt(st.nextToken());
			boolean isTrue = true;
			ArrayList<Integer>[] map = new ArrayList[V + 1];
			for (int j = 0; j <= V; j++) {
				map[j] = new ArrayList<>();
			}
			for (int j = 0; j < E; j++) {
				st = new StringTokenizer(br.readLine());
				int start = Integer.parseInt(st.nextToken());
				int end = Integer.parseInt(st.nextToken());
				map[start].add(end);
				map[end].add(start);
			}
			int[] color = new int[V + 1];
			for (int j = 1; j <= V; j++) {
				if (color[j] == 0) {
					Queue<Pair> q = new LinkedList<>();
					color[j] = 1;
					q.add(new Pair(j, 1));
					while (!q.isEmpty() && isTrue) {
						Pair pair = q.poll();
						for (int a : map[pair.x]) {
							if (color[a] == pair.color) {
								isTrue = false;
								break;
							} else if (color[a] == 0){
								color[a] = pair.color == 1? -1 : 1;
								q.add(new Pair(a, color[a]));
							}
						}
					}
				}
			}
			if (isTrue)
				System.out.println("YES");
			else
				System.out.println("NO");

		}
 	}
}

class Pair{
	int x;
	int color;

	public Pair(int x, int color) {
		this.x = x;
		this.color = color;
	}

}
