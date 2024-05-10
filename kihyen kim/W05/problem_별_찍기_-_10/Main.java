import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size
		int size = Integer.parseInt(br.readLine());
		
		// INIT cantor lamda function
		Function<Integer, Boolean[][]> funcGenerateCantorMatrix = new Function<Integer, Boolean[][]>() {

			@Override
			public Boolean[][] apply(Integer size) {
				Boolean[][] arrCantorSet = new Boolean[size][size];
				for (Boolean[] row : arrCantorSet)
				    Arrays.fill(row, true);
				
				cantor(arrCantorSet, 0, 0, arrCantorSet.length);
				return arrCantorSet;
			}

			public void cantor(Boolean[][] arr,	int idxStartX, int idxStartY, int len) {
				int lenDivided = len / 3;
				if (lenDivided > 0) {
					// BLANK only index between 1/3 to 2/3
					for (int y = idxStartY + lenDivided; y < idxStartY + lenDivided*2; y++)
						for (int x = idxStartX + lenDivided; x < idxStartX + lenDivided*2; x++)
							arr[x][y] = false;

					// RECURSION...
					for (int y = idxStartY; y < idxStartY + len; y += lenDivided) {
						for (int x = idxStartX; x < idxStartX + len; x += lenDivided) {
							// EXCLUDE that have already been blanked
							if (x == idxStartX + lenDivided && y == idxStartY + lenDivided)
								continue;

							cantor(arr, x, y, lenDivided);
						}
					}
				}
			}

		};

		// GENERATE
		Boolean[][] matrix = funcGenerateCantorMatrix.apply(size);
		for (Boolean[] row : matrix) {
			for (Boolean point : row)
				sb.append(point ? "*" : " ");
			sb.append("\n");
		}

		// PRINT
		System.out.println(sb);

	}

}