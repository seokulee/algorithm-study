import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			Queue<Node> q = new LinkedList<>();

			q.add(new Node(a, 0, ""));
			String res = "";
			boolean[] visited = new boolean[100000];
			while (!q.isEmpty()) {
				Node now = q.poll();
				if (visited[now.num])
					continue;
				visited[now.num] = true;
				if (now.num == b) {
					res = now.com;
					break;
				}
				int num = now.num;
				int nextNum = now.cnt + 1;
				int D = D(num);
				int S = S(num);
				int L = L(num);
				int R = R(num);
				if (!visited[D])
					q.add(new Node(D, nextNum, now.com + "D"));
				if (!visited[S])
					q.add(new Node(S, nextNum, now.com + "S"));
				if (!visited[L])
					q.add(new Node(L, nextNum, now.com + "L"));
				if (!visited[R])
					q.add(new Node(R, nextNum, now.com + "R"));
			}
			sb.append(res).append("\n");
		}
		System.out.println(sb);
	}

	static int D (int a) {
		return (a * 2) % 10000;
	}

	static int S (int a) {
		return a == 0 ? 9999 : a - 1;
	}

	static int L (int a) {
		int dum = a % 1000;
		a = a / 1000 + dum * 10;
		return a;
	}

	static int R (int a) {
		a = a / 10 + a % 10 * 1000;
		return a;
	}
}

class Node implements Comparable<Node>{
	int num;
	int cnt;
	String com;

	public Node(int num, int cnt, String com) {
		this.num = num;
		this.cnt = cnt;
		this.com = com;
	}

	@Override
	public int compareTo (Node o) {
		return this.cnt - o.cnt;
	}
}
