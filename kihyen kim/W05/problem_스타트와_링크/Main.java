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
		int[][] synergy = new int[size][size];
		{
			for (int i=0; i<size; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j=0; j<size; j++)
					synergy[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		// INIT depth first search lamda function
		Function<Object[], TreeSet<Integer>> funcDepthFirstSearch = new Function<Object[], TreeSet<Integer>>() {

			int[][] synergy;
			boolean[] arrVisited;

			TreeSet<Integer> result;

			@Override
			public TreeSet<Integer> apply(Object[] params) {
				result = new TreeSet<Integer>();

				this.synergy = (int[][]) params[0];
				arrVisited = new boolean[synergy.length];

				dfs(0, 0);
				return result;
			}

			public void dfs(int idx, int depth) {
				if (result.contains(0))
					return;
					
				if (depth == synergy.length/2) {
					int powerA = 0, powerB = 0;
					for (int i = 0; i < synergy.length - 1; i++) {
						for (int j = i + 1; j < synergy.length; j++) { 
							if (arrVisited[i] == true && arrVisited[j] == true) {
								powerA += synergy[i][j];
								powerA += synergy[j][i];
							}
							else
							if (arrVisited[i] == false && arrVisited[j] == false) {
								powerB += synergy[i][j];
								powerB += synergy[j][i];
							}
						}
					}
					result.add(Math.abs(powerA - powerB));

					return;
				}

				for (int i = idx; i < synergy.length; i++) {
					if (!arrVisited[i]) {
						arrVisited[i] = true;
						
						dfs(i+1, depth+1);
						
						arrVisited[i] = false;
					}
				}
			}

		};

		// GENERATE
		Object[] params = new Object[] { synergy };
		TreeSet<Integer> results = funcDepthFirstSearch.apply(params);

		// PRINT
		System.out.println(results.first());

	}

}