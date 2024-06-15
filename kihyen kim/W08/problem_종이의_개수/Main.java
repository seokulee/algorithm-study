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
		int[][] coloredPaper = new int[size][size];
		for (int i = 0; i < size; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < size; j++)
				coloredPaper[i][j] = Integer.parseInt(st.nextToken());
		}

		// INIT lamda function
		Function<Object, Object[]> funcGenerateOrigamiPaper = new Function<Object, Object[]>() {

			int[][] coloredPaper;
			int cntRed, cntGreen, cntBlue;

			@Override
			public Object[] apply(Object param) {
				this.coloredPaper = (int[][]) param;
				this.cntRed = this.cntGreen = this.cntBlue = 0;

				recursion(0, 0, coloredPaper.length);

				return new Object[] { cntRed, cntGreen, cntBlue };
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
					if (coloredPaper[idxY][idxX] == -1)
						cntRed++;
					else if (coloredPaper[idxY][idxX] == 0)
						cntGreen++;
					else
						cntBlue++;

					return;
				}

				size /= 3;
				recursion(idxY, idxX, size);
				recursion(idxY, idxX + size, size);
				recursion(idxY, idxX + size*2, size);
				recursion(idxY + size, idxX, size);
				recursion(idxY + size, idxX + size, size);
				recursion(idxY + size, idxX + size*2, size);
				recursion(idxY + size*2, idxX, size);
				recursion(idxY + size*2, idxX + size, size);
				recursion(idxY + size*2, idxX + size*2, size);
			}
		};

		// CALC & PRINT
		Object[] result = funcGenerateOrigamiPaper.apply(coloredPaper);
		sb
			.append((int)result[0])
			.append("\n")
			.append((int)result[1])
			.append("\n")
			.append((int)result[2]);
		System.out.println(sb);

	}

}