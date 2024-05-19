import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT sudoku, blanks
		int[][] sudoku = new int[9][9];
		List<Integer> listBlanks = new ArrayList<>();
		Set<Integer>[] setRows = new HashSet[9];
		Set<Integer>[] setCols = new HashSet[9];
		Set<Integer>[] setPart = new HashSet[9];
		for (int i = 0; i < sudoku.length; i++) {
			setRows[i] = new HashSet<Integer>();
			setCols[i] = new HashSet<Integer>();
			setPart[i] = new HashSet<Integer>();
		}
		for (int y = 0; y < sudoku.length; y++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int x = 0; x < sudoku[y].length; x++) {
				int num = Integer.parseInt(st.nextToken());

				sudoku[y][x] = num;

				if (num > 0) {
					setRows[y].add(num);
					setCols[x].add(num);
					setPart[(x / 3) * 3 + (y / 3)].add(num);
				}
				else
					listBlanks.add(y * 10 + x);
			}
		}

		// INIT & RUN depth first search lamda function
		Runnable funcSudokuSolver = new Runnable() {
			@Override
			public void run() { dfs(0); }
			public boolean dfs(int idxBlank) {
				if (idxBlank == listBlanks.size())
					return true;

				int y = listBlanks.get(idxBlank) / 10;
				int x = listBlanks.get(idxBlank) % 10;
                
				for (int i = 1; i < 10; i++) {
					if (!setRows[y].contains(i) &&
						!setCols[x].contains(i) &&
						!setPart[(x / 3) * 3 + (y / 3)].contains(i)) {
						
						// TRY substituting
						sudoku[y][x] = i;
						setRows[y].add(i);
						setCols[x].add(i);
						setPart[(x / 3) * 3 + (y / 3)].add(i);

						boolean isPlacable = dfs(idxBlank + 1);
						if (isPlacable)
							return true;
						
						// ROLLBACK
						sudoku[y][x] = 0;
						setRows[y].remove(i);
						setCols[x].remove(i);
						setPart[(x / 3) * 3 + (y / 3)].remove(i);
					}
				}
				return false;
			}
		};
		funcSudokuSolver.run();

		// PRINT
		for (int[] row : sudoku) {
			for (int col : row)
				sb.append(col).append(" ");
			sb.append("\n");
		}
		System.out.println(sb);

	}

}

/*
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT sudoku, blanks
		int[][] sudoku = new int[9][9];
		int[] rows = new int[9];
		int[] cols = new int[9];
		int[] parts = new int[9];
		List<Integer> listBlanks = new ArrayList<>();
		for (int y = 0; y < sudoku.length; y++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int x = 0; x < sudoku[y].length; x++) {
				int num = Integer.parseInt(st.nextToken());

				sudoku[y][x] = num;

				if (num > 0) {
					rows[y] |= (1 << num);
					cols[x] |= (1 << num);
					parts[(x / 3) * 3 + (y / 3)] |= (1 << num);
				}
				else
					listBlanks.add(y * 10 + x);
			}
		}

		// INIT & RUN depth first search lamda function
		Runnable funcSudokuSolver = new Runnable() {
			@Override
			public void run() { dfs(0); }
			public boolean dfs(int idxBlank) {
				if (idxBlank == listBlanks.size())
					return true;

				int y = listBlanks.get(idxBlank) / 10;
				int x = listBlanks.get(idxBlank) % 10;
				
				for (int num = 1; num <= 9; num++) {
					if (( rows[y] & (1 << num) ) == 0 &&
						( cols[x] & (1 << num) ) == 0 &&
						( parts[(x / 3) * 3 + (y / 3)] & (1 << num) ) == 0) {
						
						// TRY substituting
						sudoku[y][x] = num;
						rows[y] |= (1 << num);
						cols[x] |= (1 << num);
						parts[(x / 3) * 3 + (y / 3)] |= (1 << num);

						boolean isPlacable = dfs(idxBlank + 1);
						if (isPlacable)
							return true;
						
						// ROLLBACK
						sudoku[y][x] = 0;
						rows[y] &= ~(1 << num);
						cols[x] &= ~(1 << num);
						parts[(x / 3) * 3 + (y / 3)] &= ~(1 << num);
						
					}
				}
				return false;
			}
		};
		funcSudokuSolver.run();

		// PRINT
		for (int[] row : sudoku) {
			for (int col : row)
				sb.append(col).append(" ");
			sb.append("\n");
		}
		System.out.println(sb);

	}

}
*/