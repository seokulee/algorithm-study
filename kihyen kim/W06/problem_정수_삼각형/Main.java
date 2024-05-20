import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, current line array
		int size = Integer.parseInt(br.readLine());
		int[][] arrCurrentLine = new int[size][500];
		for (int i = 0; i < size; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j <= i; j++) {
				int num = Integer.parseInt(st.nextToken());

				if (i == 0)
					arrCurrentLine[0][0] = num;
				else
				if (j == 0)
					arrCurrentLine[i][j] = num + arrCurrentLine[i - 1][0];
				else
				if (j == i)
					arrCurrentLine[i][j] = num + arrCurrentLine[i - 1][i - 1];
				else
					arrCurrentLine[i][j] = num + Math.max(arrCurrentLine[i - 1][j - 1], arrCurrentLine[i - 1][j]);
			}
		}

		// PRINT
		int max = Arrays.stream(arrCurrentLine[size - 1]).max().orElse(0);
		System.out.println(max);

	}

}