import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size
		int size = Integer.parseInt(br.readLine());

		// INIT depth first search lamda function
		Function<Integer, Integer> funcNQueenSolver = new Function<Integer, Integer>() {

			boolean[][] board;

			int result;

			@Override
			public Integer apply(Integer size) {
				this.board = new boolean[size][size];
				this.result = 0;

				if (size == 1)
					return 1;

				dfs(size, 0);
				return result;
			}

			public void dfs(int size, int row) {
				if (size == row) {
					result++;
					return;
				}

				for (int col = 0; col < size; col++) {
					boolean isPlacable = true;
					{
						// CHECK vertical
						for (int i = row; isPlacable && i >= 0; i--)
							if (board[i][col])
								isPlacable = false;

						// CHECK upper left direction
						for (int i = row, j = col; isPlacable && i >= 0 && j >= 0; i--, j--)
							if (board[i][j])
								isPlacable = false;

						// CHECK upper right direction
						for (int i = row, j = col; isPlacable && i >= 0 && j < size; i--, j++)
							if (board[i][j])
								isPlacable = false;
					}

					if (isPlacable) {
						board[row][col] = true;

						dfs(size, row + 1);

						board[row][col] = false;
					}
				}
			}

		};

		// PRINT
		System.out.println(funcNQueenSolver.apply(size));

	}

}