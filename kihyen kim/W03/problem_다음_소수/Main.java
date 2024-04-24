import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static long getNearestPrimeNumber(long num) {

		if (num == 0 || num == 1)
			return 2;

		while (true) {
			boolean isPrimeNumber = true;

			for (int i = 2; i <= Math.sqrt(num); i++) {
				if (num % i == 0) {
					isPrimeNumber = false;
					break;
				}
			}

			if (isPrimeNumber)
				return num;

			num++;
		}

	}

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size
		int size = Integer.parseInt(br.readLine());

		// CALC, PRINT
		for (int i = 0; i < size; i++) {
			long npn = getNearestPrimeNumber(Long.parseLong(br.readLine()));
			sb.append(npn).append("\n");
		}
		System.out.println(sb);

	}

}