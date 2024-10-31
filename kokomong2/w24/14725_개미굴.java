
import java.io.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {

	static Set<Node> tree;
	static BufferedWriter bw;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		bw = new BufferedWriter(new OutputStreamWriter(System.out));
		tree = new TreeSet<>();
		int N = Integer.parseInt(br.readLine());
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int num = Integer.parseInt(st.nextToken());
			Set<Node> nowSet = tree;
			for (int j = 0; j < num; j++) {
				String nowStr = st.nextToken();
				boolean isSame = false;
				for (Node node : nowSet) {
					if (Objects.equals(node.str, nowStr)) {
						nowSet = node.child;
						isSame = true;
						break;
					}
				}
				if (!isSame) {
					Node node = new Node(nowStr);
					nowSet.add(node);
					nowSet = node.child;
				}
			}
		}

		printTree(tree, 0);
		bw.flush();
		bw.close();
		br.close();
	}

	static void printTree(Set<Node> tree, int dept) throws IOException {

		if (tree.isEmpty())
			return;

		for (Node node : tree) {
			for (int i = 0; i < dept; i++) {
				bw.write("--");
			}
			bw.write(node.str + "\n");
			printTree(node.child, dept + 1);
		}
	}
}

class Node implements Comparable<Node> {
	String str;
	Set<Node> child;

	public Node(String str) {
		this.str = str;
		this.child = new TreeSet<>();
	}

	@Override
	public int compareTo(Node o) {
		return this.str.compareTo(o.str);
	}
}
