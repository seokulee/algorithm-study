import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, stacks
		int size = Integer.parseInt(br.readLine());
		String[] nums = br.readLine().split(" ");
		Stack<Integer> stackCurrentLine = new Stack<Integer>();
		Stack<Integer> stackBlankedLine = new Stack<Integer>();
		for(int i=size-1; i>=0; i--)
			stackCurrentLine.add( Integer.parseInt(nums[i]) );

		// RUN
		int index = 1;
		while(index <= size)
		{
			if (!stackCurrentLine.isEmpty() && stackCurrentLine.peek() == index) {
				// System.out.println("index"+index+" completely poped");
				stackCurrentLine.pop();
				index++;
			}
			else
			if (!stackBlankedLine.isEmpty() && stackBlankedLine.peek() == index) {
				// System.out.println("index"+index+" completely poped");
				stackBlankedLine.pop();
				index++;
			}
			else
			if (!stackCurrentLine.isEmpty()) {
				// System.out.println("stackBlankedLine added "+stackCurrentLine.peek());
				stackBlankedLine.add(stackCurrentLine.peek());
				stackCurrentLine.pop();
			}
			else
				break;
		}
		boolean result = (stackCurrentLine.isEmpty() && stackBlankedLine.isEmpty());

		// PRINT
		System.out.println(result ? "Nice" : "Sad");

	}

}