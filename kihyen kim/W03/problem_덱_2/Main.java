import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, queue
		int size = Integer.parseInt(br.readLine());
		ArrayDeque<Integer> deck = new ArrayDeque<Integer>();

		// STATE MACHINE
		for(int i=0; i<size; i++)
		{
			String comand = br.readLine();
			int num = (comand.contains(" ")) ? Integer.parseInt(comand.split(" ")[1]) : 0;
			
			switch(comand.charAt(0)) {
			case '1' : // push front
				deck.addFirst(num);
				break;
			case '2' : // push back
				deck.addLast(num);
				break;
			case '3' : // pop front
				sb.append(deck.isEmpty() ? -1 : deck.removeFirst()).append("\n");
				break;
			case '4' : // pop back
				sb.append(deck.isEmpty() ? -1 : deck.removeLast()).append("\n");
				break;
			case '5' : // print size
				sb.append(deck.size()).append("\n");
				break;
			case '6' : // isEmpty
				sb.append(deck.isEmpty() ? 1 : 0).append("\n");
				break;
			case '7' : // peek front
				sb.append(deck.isEmpty() ? -1 : deck.peekFirst()).append("\n");
				break;
			case '8' : // peek back
				sb.append(deck.isEmpty() ? -1 : deck.peekLast()).append("\n");
				break;
			}
		}

		// PRINT
		System.out.println(sb);

	}

}