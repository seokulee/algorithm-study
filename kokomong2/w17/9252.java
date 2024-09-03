import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input1 = br.readLine();
		String input2 = br.readLine();

		int input1Len = input1.length();
		int input2Len = input2.length();

		int[][] map = new int[input2Len + 1][input1Len + 1];

		for (int i = 1; i <= input2Len; i++) {
			char c2 = input2.charAt(i - 1);
			for (int j = 1; j <= input1Len; j++) {
				char c1 = input1.charAt(j - 1);
				if (c2 == c1)
					map[i][j] = map[i - 1][j - 1] + 1;
				else
					map[i][j] = Math.max(map[i - 1][j], map[i][j - 1]);
			}
		}

		System.out.println(map[input2Len][input1Len]);

		Stack<Character> stack = new Stack<>();
		int y = input2Len;
		int x = input1Len;
		while (x > 0 && y > 0) {
			if (input1.charAt(x - 1) == input2.charAt(y - 1)) {
				stack.push(input1.charAt(x - 1));
				x--;
				y--;
			} else if (map[y - 1][x] > map[y][x - 1]) {
				y--;
			} else {
				x--;
			}
		}

		StringBuilder sb = new StringBuilder();
		while (!stack.isEmpty()) {
			sb.append(stack.pop());
		}
		System.out.println(sb);
	}
}
