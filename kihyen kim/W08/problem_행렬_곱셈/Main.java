import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		// INIT size of n, size of m, matrix n*m
		st = new StringTokenizer(br.readLine());
		int sizeN = Integer.parseInt(st.nextToken());
		int sizeM = Integer.parseInt(st.nextToken());
		int[][] matrixNM = new int[sizeN][sizeM];
		for (int i = 0; i < sizeN; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < sizeM; j++)
				matrixNM[i][j] = Integer.parseInt(st.nextToken());
		}

		// INIT size of k, matrix m*k
		st = new StringTokenizer(br.readLine());
		st.nextToken(); // skip duplicated sizeM
		int sizeK = Integer.parseInt(st.nextToken());
		int[][] matrixMK = new int[sizeM][sizeK];
		for (int i = 0; i < sizeM; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < sizeK; j++)
				matrixMK[i][j] = Integer.parseInt(st.nextToken());
		}

		// CALC
		int[][] result = new int[sizeN][sizeK];
		for (int n = 0; n < sizeN; n++) {
			for (int k = 0; k < sizeK; k++) {
				int sum = 0;
				for (int m = 0; m < sizeM; m++)
					sum += matrixNM[n][m] * matrixMK[m][k];
				
				result[n][k] = sum;
			}
		}

		// PRINT
		for (int[] row : result) {
			for (int num : row)
				sb.append(num).append(" ");
			sb.append("\n");
		}
		System.out.println(sb);

	}

}