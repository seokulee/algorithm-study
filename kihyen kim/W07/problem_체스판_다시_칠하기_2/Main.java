import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size of y, size of x, size of required square
		st = new StringTokenizer(br.readLine());
		int sizeY = Integer.parseInt(st.nextToken());
		int sizeX = Integer.parseInt(st.nextToken());
		int sizeRequiredSquare = Integer.parseInt(st.nextToken());

		// INIT dynamic programming array
		char[][] board = new char[sizeY][sizeX];
		int[][] dpSum_if00Black = new int[sizeY+1][sizeX+1];
		int[][] dpSum_if00White = new int[sizeY+1][sizeX+1];
		for (int y = 0; y < sizeY; y++) {
			String line = br.readLine();
			for (int x = 0; x < sizeX; x++)
			{
				board[y][x] = line.charAt(x);

				dpSum_if00Black[y + 1][x + 1] = (board[y][x] == ((y + x) % 2 == 0 ? 'B' : 'W') ? 0 : 1) + dpSum_if00Black[y + 1][x] + dpSum_if00Black[y][x + 1] - dpSum_if00Black[y][x];
				dpSum_if00White[y + 1][x + 1] = (board[y][x] == ((y + x) % 2 == 0 ? 'W' : 'B') ? 0 : 1) + dpSum_if00White[y + 1][x] + dpSum_if00White[y][x + 1] - dpSum_if00White[y][x];
			}
		}

		// CALC
		int result = Integer.MAX_VALUE;
		for (int y = 1; y <= sizeY - sizeRequiredSquare + 1; y++) {
			for (int x = 1; x <= sizeX - sizeRequiredSquare + 1; x++)
			{
				int endY = y + sizeRequiredSquare - 1;
				int endX = x + sizeRequiredSquare - 1;

				result = Math.min( result, dpSum_if00Black[endY][endX] - dpSum_if00Black[y - 1][endX] - dpSum_if00Black[endY][x - 1] + dpSum_if00Black[y - 1][x - 1] );
				result = Math.min( result, dpSum_if00White[endY][endX] - dpSum_if00White[y - 1][endX] - dpSum_if00White[endY][x - 1] + dpSum_if00White[y - 1][x - 1] );
			}
		}

		// PRINT
		System.out.println(result);

	}

}