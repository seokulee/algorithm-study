import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, priority queue
		int size = Integer.parseInt(br.readLine());
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>(
			(o1, o2) -> {
				int abs1 = Math.abs(o1);
				int abs2 = Math.abs(o2);

				if (abs1 == abs2)
					return Integer.compare(o1, o2);

				return Integer.compare(abs1, abs2);
			}
			/* without lambda
			new Comparator<Integer>() {
				@Override
				public int compare(Integer o1, Integer o2){
					int abs1 = Math.abs(o1);
					int abs2 = Math.abs(o2);
			
					if (abs1 == abs2)
						return Integer.compare(o1, o2);
					
					return Integer.compare(abs1, abs2);
				}
			}
			*/
		);

		// RUN
		for (int i = 0; i < size; i++) {
			int num = Integer.parseInt(br.readLine());
			if (num == 0)
				sb.append(pq.isEmpty() ? 0 : pq.poll()).append('\n');
			else
				pq.add(num);
		}

		// PRINT
		System.out.println(sb);

	}

}