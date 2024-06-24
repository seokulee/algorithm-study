import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, priority queue
		int size = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();

		// RUN
		for (int i = 0; i < size; i++) {
			int num = Integer.parseInt(br.readLine());
			if (num == 0)
				sb.append( pq.isEmpty() ? 0 : pq.poll() ).append('\n');
			else
				pq.add(num);
		}

		// PRINT
		System.out.println(sb);

	}

}