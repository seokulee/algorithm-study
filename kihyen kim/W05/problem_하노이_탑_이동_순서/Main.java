import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size
		int size = Integer.parseInt(br.readLine());
		
		// INIT hanoi lamda function
		Function<Integer, List<String>> funcGenerateHanoiTower = new Function<Integer, List<String>>() {

			List<String> result = new ArrayList<String>();
			
			@Override
			public List<String> apply(Integer size) {
				result.removeAll(result);
				
				hanoi(size, 1, 3, 2);
				return result;
			}

			public void hanoi(int n, int from, int to, int through) {
				if (n == 0)
					return;

				hanoi(n - 1, from, through, to);

				result.add(from + " " + to);
				// result.add(from + " " + to + " / disc:" + n);

				hanoi(n - 1, through, to, from);
			}

		};

		// GENERATE
		List<String> moves = funcGenerateHanoiTower.apply(size);

		// PRINT
		sb.append(moves.size()).append("\n");
		for (String s : moves) {
			sb.append(s).append("\n");
		}
		System.out.println(sb);

	}

}