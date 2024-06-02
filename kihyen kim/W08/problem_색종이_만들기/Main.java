import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		// INIT size, colored paper
		int size = Integer.parseInt(br.readLine());
		boolean[][] coloredPaper = new boolean[size][size];
		for (int i = 0; i < size; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < size; j++)
				coloredPaper[i][j] = st.nextToken().equals("1");
		}

		// INIT lamda function
		Function<Object, Object[]> funcGenerateOrigamiPaper = new Function<Object, Object[]>() {

			boolean[][] coloredPaper;
			int cntWhite, cntBlue;

			@Override
			public Object[] apply(Object param) {
				this.coloredPaper = (boolean[][]) param;
				this.cntWhite = this.cntBlue = 0;

				recursion(0, 0, coloredPaper.length);

				return new Object[] { cntWhite, cntBlue };
			}

			public void recursion(int idxY, int idxX, int size) {
				boolean isMono = true;
				for (int y = idxY; y < idxY + size; y++) {
					for (int x = idxX; x < idxX + size; x++)
						if (coloredPaper[y][x] != coloredPaper[idxY][idxX]) {
							isMono = false;
							break;
						}
				}

				if (isMono) {
					if (coloredPaper[idxY][idxX])
						cntBlue++;
					else
						cntWhite++;

					return;
				}

				recursion(idxY, idxX, size / 2);
				recursion(idxY, idxX + size / 2, size / 2);
				recursion(idxY + size / 2, idxX, size / 2);
				recursion(idxY + size / 2, idxX + size / 2, size / 2);
			}
		};

		// CALC & PRINT
		Object[] result = funcGenerateOrigamiPaper.apply(coloredPaper);
		sb
			.append((int)result[0])
			.append("\n")
			.append((int)result[1]);
		System.out.println(sb);

	}

}