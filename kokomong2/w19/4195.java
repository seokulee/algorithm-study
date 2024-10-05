import java.io.*;
import java.util.*;

public class Main {
	private static final HashMap<String, Integer> names = new HashMap<>();
	private static int[] friendsCnt;
	private static int[] parents;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int tc = Integer.parseInt(br.readLine());
		while (tc-- > 0) {
			int n = Integer.parseInt(br.readLine());

			names.clear();
			parents = new int[n * 2];
			friendsCnt = new int[n * 2];
			Arrays.fill(friendsCnt, 1);

			for (int i = 0; i < n * 2; i++) {
				parents[i] = i;
			}

			int nowIdx = 0;

			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());

				String friend1 = st.nextToken();
				String friend2 = st.nextToken();

				if (!names.containsKey(friend1)) {
					names.put(friend1, nowIdx++);
				}

				if (!names.containsKey(friend2)) {
					names.put(friend2, nowIdx++);
				}

				int idx1 = names.get(friend1);
				int idx2 = names.get(friend2);
				int parentsA = findParents(idx1);
				int parentsB = findParents(idx2);
				if (parentsA == parentsB) {
					sb.append(friendsCnt[parentsA]).append("\n");
				} else {
					int ans = unionParents(idx1, idx2);
					sb.append(friendsCnt[ans]).append("\n");
				}
			}
		}
		System.out.println(sb);
	}

	private static int unionParents(int a, int b) {
		a = findParents(a);
		b = findParents(b);

		if (a < b) {
			friendsCnt[a] += friendsCnt[b];
			return parents[b] = a;
		}
		friendsCnt[b] += friendsCnt[a];
		return parents[a] = b;
	}

	private static int findParents(int x) {
		if (parents[x] == x) return x;
		return parents[x] = findParents(parents[x]);
	}
}
