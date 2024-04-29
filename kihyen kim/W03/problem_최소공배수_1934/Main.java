import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static int getLcm(int a, int b) {
		if (a < b) {
			int temp = a;
			a = b;
			b = temp;
		}

		int lcm = 0;
		while ((lcm += a) % b != 0)
			;

		return lcm;
	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, result
		int size = Integer.parseInt(br.readLine());
		int[] result = new int[size];

		// CALC
		for (int i = 0; i < size; i++) {
			String[] nums = br.readLine().split(" ");
			int num1 = Integer.parseInt(nums[0]);
			int num2 = Integer.parseInt(nums[1]);

			result[i] = getLcm(num1, num2);
		}

		// PRINT
		for (int r : result)
			sb.append(r).append("\n");
		System.out.println(sb);

	}

}