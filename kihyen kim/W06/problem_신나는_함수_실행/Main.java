import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT function
		Function<Object[], Integer> funcDynamicProgramming = new Function<Object[], Integer>() {

			int[][][] dp = new int[21][21][21];

			@Override
			public Integer apply(Object[] params) { return solveByDP((int)params[0], (int)params[1], (int)params[2]); }
			
			int solveByDP(int a, int b, int c) {
				if (a <= 0 || b <= 0 || c <= 0)
					return 1;
				if (a > 20 || b > 20 || c > 20)
					a = b = c = 20;
				
				if (dp[a][b][c] != 0) // if already cached
					return dp[a][b][c];

				return dp[a][b][c] = (a < b && b < c)
						? solveByDP(a, b, c - 1) + solveByDP(a, b - 1, c - 1) - solveByDP(a, b - 1, c)
						: solveByDP(a - 1, b, c) + solveByDP(a - 1, b - 1, c) + solveByDP(a - 1, b, c - 1) - solveByDP(a - 1, b - 1, c - 1)
						;
			}
		};

		// READ & PRINT
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			if (a == -1 && b == -1 && c == -1)
				break;

			sb
				.append("w(")
				.append(a).append(", ").append(b).append(", ").append(c)
				.append(") = ")
				.append( funcDynamicProgramming.apply(new Object[] {a, b, c}) )
				.append("\n")
				;
		}
		System.out.println(sb);
		
	}

}