import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, stack
		Stack<Integer> stack = new Stack<Integer>();

		// ASSESS valid parenthesis string
		String str;
		while (!(str = br.readLine()).equals("."))
		{
			boolean isValid = true;
			char[] charArray = str.toCharArray();
			for (char c : charArray) {
				if (c == '(')
					stack.push(1);
				else
				if (c == '[')
					stack.push(2);
				else
				if (c == ')') {
					if (!stack.isEmpty() && stack.peek() == 1)
						stack.pop();
					else {
						isValid = false;
						break;
					}
				}
				else
				if (c == ']') {
					if (!stack.isEmpty() && stack.peek() == 2)
						stack.pop();
					else {
						isValid = false;
						break;
					}
				}
			}
			
			if (!stack.isEmpty()) {
				isValid = false;
				while (!stack.isEmpty())
					stack.pop();
			}
			
			sb.append(isValid ? "yes\n" : "no\n");
		}

		// PRINT
		System.out.println(sb);

	}

}