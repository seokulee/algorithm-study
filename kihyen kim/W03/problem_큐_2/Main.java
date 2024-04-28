import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, queue
		int size = Integer.parseInt(br.readLine());
		Queue<Integer> queue = new LinkedList<Integer>();

		// STATE MACHINE
		for(int i=0; i<size; i++)
		{
			String comand = br.readLine();
			int num = (comand.contains(" ")) ? Integer.parseInt(comand.split(" ")[1]) : 0;
			
			switch(comand.substring(0,2)) {
			case "pu" : // push
				queue.add(num);
				break;
			case "po" : // pop
				sb.append(queue.isEmpty() ? -1 : queue.remove()).append("\n");
				break;
			case "si" : // size
				sb.append(queue.size()).append("\n");
				break;
			case "em" : // empty
				sb.append(queue.isEmpty() ? 1 : 0).append("\n");
				break;
			case "fr" : // front
				sb.append(queue.isEmpty() ? -1 : ((LinkedList<Integer>)queue).getFirst()).append("\n");
				break;
			case "ba" : // back
				sb.append(queue.isEmpty() ? -1 : ((LinkedList<Integer>)queue).getLast()).append("\n");
				break;
			}
		}

		// PRINT
		System.out.println(sb);

	}

}