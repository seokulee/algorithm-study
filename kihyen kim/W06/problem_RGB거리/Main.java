import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, cost array
		int size = Integer.parseInt(br.readLine());
		int[][] arrCosts = new int[size][3];
		final int R_COST = 0;
		final int G_COST = 1;
		final int B_COST = 2;
		for (int i = 0; i < size; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			arrCosts[i][R_COST] = Integer.parseInt(st.nextToken());
			arrCosts[i][G_COST] = Integer.parseInt(st.nextToken());
			arrCosts[i][B_COST] = Integer.parseInt(st.nextToken());

			if (i != 0) {
				arrCosts[i][R_COST] += Math.min(arrCosts[i - 1][G_COST], arrCosts[i - 1][B_COST]);
				arrCosts[i][G_COST] += Math.min(arrCosts[i - 1][R_COST], arrCosts[i - 1][B_COST]);
				arrCosts[i][B_COST] += Math.min(arrCosts[i - 1][R_COST], arrCosts[i - 1][G_COST]);
			}
		}

		// PRINT
		int sumA = arrCosts[size-1][R_COST];
		int sumB = arrCosts[size-1][G_COST];
		int sumC = arrCosts[size-1][B_COST];
		System.out.println(Math.min(Math.min(sumA, sumB), sumC));
		
	}

}