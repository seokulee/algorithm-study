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

		// STATE MACHINE
		for (int i = 0; i < size; i++) {
			String[] comand = br.readLine().split(" ");
			switch (Integer.parseInt(comand[0])) {
			case 1:
				stack.push(Integer.parseInt(comand[1]));
				break;
			case 2:
				sb.append(stack.size() == 0 ? -1 : stack.pop()).append("\n");
				break;
			case 3:
				sb.append(stack.size()).append("\n");
				break;
			case 4:
				sb.append(stack.size() == 0 ? 1 : 0).append("\n");
				break;
			case 5:
				sb.append(stack.size() == 0 ? -1 : stack.peek()).append("\n");
				break;
			}
		}

		// PRINT
		System.out.println(sb);

	}

}