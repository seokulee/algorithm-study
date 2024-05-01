import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, stack
		int size = Integer.parseInt(br.readLine());
		Stack<Integer> stack = new Stack<Integer>();
		for (int i = 0; i < size; i++) {
			int num = Integer.parseInt(br.readLine());
			switch (num) {
			case 0:
				stack.pop();
				break;
			default:
				stack.push(num);
			}
		}

		// PRINT
		int result = 0;
		while (stack.size() != 0)
			result += stack.pop();
		System.out.println(result);

	}

}