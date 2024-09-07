import java.io.*;
import java.util.*;

public class Main {
	static StringBuilder sb;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		sb = new StringBuilder();
		int rootNum = Integer.parseInt(br.readLine());
		Node root = new Node(rootNum);
		String input;
		while (true) {
			input = br.readLine();
			if (input == null || input.equals(""))
				break;
			root.insert(Integer.parseInt(input));
		}

		postOrder(root);
		System.out.println(sb);
	}

	public static void postOrder (Node node) {
		if (node == null)
			return ;
		postOrder(node.left);
		postOrder(node.right);
		sb.append(node.value).append("\n");
	}
}

class Node {
	int value;
	Node left;
	Node right;
	public Node(int value) {
		this.value = value;
	}

	public void insert (int n) {
		if (n > this.value) {
			if (this.right == null)
				this.right = new Node(n);
			else
				this.right.insert(n);
		} else {
			if (this.left == null)
				this.left = new Node(n);
			else
				this.left.insert(n);
		}
	}
}
