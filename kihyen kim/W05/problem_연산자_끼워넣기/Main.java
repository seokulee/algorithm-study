import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, operands, operators
		int size = Integer.parseInt(br.readLine());
		int[] arrOperands = new int[size];
		char[] arrOperators = new char[size - 1];
		{
			StringTokenizer st;

			st = new StringTokenizer(br.readLine());
			for (int i = 0; st.hasMoreTokens(); i++)
				arrOperands[i] = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			int i = 0;
			for (int numOp = Integer.parseInt(st.nextToken()); numOp > 0; numOp--)
				arrOperators[i++] = '+';
			for (int numOp = Integer.parseInt(st.nextToken()); numOp > 0; numOp--)
				arrOperators[i++] = '-';
			for (int numOp = Integer.parseInt(st.nextToken()); numOp > 0; numOp--)
				arrOperators[i++] = '*';
			for (int numOp = Integer.parseInt(st.nextToken()); numOp > 0; numOp--)
				arrOperators[i++] = '/';
		}

		// INIT depth first search lamda function
		Function<Object[], TreeSet<Integer>> funcDepthFirstSearch = new Function<Object[], TreeSet<Integer>>() {

			int[] arrOperands;
			char[] arrOperators;
			boolean[] arrVisited;

			TreeSet<Integer> result;

			@Override
			public TreeSet<Integer> apply(Object[] params) {
				result = new TreeSet<Integer>();

				this.arrOperands = (int[]) params[0];
				this.arrOperators = (char[]) params[1];
				arrVisited = new boolean[arrOperators.length];

				dfs(arrOperands[0], 0);
				return result;
			}

			public void dfs(int num, int depth) {
				if (depth == arrOperators.length) {
					result.add(num);
					return;
				}

				for (int i = 0; i < arrOperators.length; i++) {
					if (!arrVisited[i]) {
						arrVisited[i] = true;

						switch (arrOperators[i]) {
						case '+':
							dfs(num + arrOperands[depth + 1], depth + 1);
							break;
						case '-':
							dfs(num - arrOperands[depth + 1], depth + 1);
							break;
						case '*':
							dfs(num * arrOperands[depth + 1], depth + 1);
							break;
						case '/':
							dfs(num / arrOperands[depth + 1], depth + 1);
						}

						arrVisited[i] = false;
					}
				}
			}

		};

		// GENERATE
		Object[] params = new Object[] { arrOperands, arrOperators };
		TreeSet<Integer> results = funcDepthFirstSearch.apply(params);

		// PRINT
		System.out.println(results.last() + "\n" + results.first());

	}

}