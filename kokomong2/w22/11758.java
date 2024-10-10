import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		List<Node> nodes = new ArrayList<>();
		for (int i = 0; i < 3; i++) {
			st = new StringTokenizer(br.readLine());
			long x = Long.parseLong(st.nextToken());
			long y = Long.parseLong(st.nextToken());
			nodes.add(new Node(x, y));
		}
		nodes.add(nodes.get(0));

		long sum1 = 0, sum2 = 0;
		for (int i = 0; i < 3; i++) {
			sum1 += (nodes.get(i).x * nodes.get(i + 1).y);
			sum2 += (nodes.get(i).y * nodes.get(i + 1).x);
		}

		long res = sum1 - sum2;
		if (res < 0)
			System.out.println(-1);
		else if (res > 0)
			System.out.println(1);
		else
			System.out.println(0);
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

