import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT range, size
		StringTokenizer st = new StringTokenizer(br.readLine());
		int range = Integer.parseInt(st.nextToken());
		int size = Integer.parseInt(st.nextToken());

		// INIT depth first search lamda function
		Function<Object[], List<String>> funcDepthFirstSearch = new Function<Object[], List<String>>() {

			int[] arr;

			List<String> result;

			@Override
			public List<String> apply(Object[] params) {
				result = new ArrayList<String>();

				int range = (int) params[0];
				int size = (int) params[1];
				arr = new int[size];

				dfs(range, size, 0);
				return result;
			}

			public void dfs(int range, int size, int depth) {
				if (depth == size) {
					String str = "";
					for (int num : arr)
						str += num + " ";

					result.add(str);
					return;
				}

				for (int i = 0; i < range; i++) {
					arr[depth] = i + 1;
					dfs(range, size, depth + 1);
				}
			}

		};

		// GENERATE
		Object[] params = new Object[] { range, size };
		List<String> sequences = funcDepthFirstSearch.apply(params);

		// PRINT
		for (String s : sequences)
			sb.append(s).append("\n");
		System.out.println(sb);

	}

}