import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, capacity, items(has weight & value)
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int capacity = Integer.parseInt(st.nextToken());
		class Item {
			public int weight;
			public int value;

			Item(int weight, int value) {
				this.weight = weight;
				this.value = value;
			}
		}
		Item[] items = new Item[size];
		for (int i = 0; i < size; i++) {
			st = new StringTokenizer(br.readLine());
			items[i] = new Item(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
		}

		// INIT dynamic programming array
		int[][] dp = new int[size + 1][capacity + 1];
		for (int i = 1; i <= size; i++) {
			Item nowItem = items[i-1]; // dp[0][c] ... = filled by zero

			for (int c = 1; c <= capacity; c++)
				if (nowItem.weight > c)
					dp[i][c] = dp[i - 1][c];
				else
					dp[i][c] = Math.max(nowItem.value, Math.max(dp[i - 1][c], dp[i - 1][c - nowItem.weight] + nowItem.value));
		}
		
		// PRINT
		System.out.println(dp[size][capacity]);

	}

}