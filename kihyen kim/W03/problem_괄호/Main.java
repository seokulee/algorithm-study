import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, stack
		int size = Integer.parseInt(br.readLine());
		Stack<Integer> stack = new Stack<Integer>();

		// ASSESS valid parenthesis string
		for (int i = 0; i < size; i++) {
			boolean isValid = true;
			char[] charArray = br.readLine().toCharArray();
			for (char c : charArray) {
				if (c == '(')
					stack.push(1);
				else if (stack.size() != 0)
					stack.pop();
				else {
					isValid = false;
					break;
				}
			}
			if (!stack.isEmpty()) {
				isValid = false;
				while (!stack.isEmpty())
					stack.pop();
			}
			sb.append(isValid ? "YES\n" : "NO\n");
		}

		// PRINT
		System.out.println(sb);

	}

}