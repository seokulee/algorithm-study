import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, deck
		int size = Integer.parseInt(br.readLine());
		ArrayDeque<Integer> deck = new ArrayDeque<Integer>();
		for(int i=1; i<=size; i++)
			deck.add(i);

		// RUN
		while(deck.size() > 1) {
			deck.removeFirst();
			deck.addLast(deck.removeFirst());
		}

		// PRINT
		System.out.println(deck.remove());

	}

}