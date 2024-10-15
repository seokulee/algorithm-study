import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st;
		List<Node> nodes = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			long x = Long.parseLong(st.nextToken());
			long y = Long.parseLong(st.nextToken());
			nodes.add(new Node(x, y));
		}
		nodes.add(nodes.get(0));

		long sum1 = 0,sum2 = 0;
		for (int i = 0; i < n; i++) {
			sum1 += (nodes.get(i).x * nodes.get(i + 1).y);
			sum2 += (nodes.get(i).y * nodes.get(i + 1).x);
		}
		double res = Math.abs((double)(sum1 - sum2)) / 2;
		System.out.printf("%.1f\n", res);
	}

	static class Node {
		long x;
		long y;

		public Node(long x, long y) {
			this.x = x;
			this.y = y;
		}
	}
}

