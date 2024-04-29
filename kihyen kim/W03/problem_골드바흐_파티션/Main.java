import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.function.Predicate;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT test cases
		int size = Integer.parseInt(br.readLine());
		int[] arrTestCase = new int[size];
		int sieveMax = 0;
		for (int i = 0; i < size; i++) {
			arrTestCase[i] = Integer.parseInt(br.readLine());
			sieveMax = (arrTestCase[i] > sieveMax) ? arrTestCase[i] : sieveMax;
		}

		// INIT sieve of eratosthenes
		Predicate<Integer> isPrimeNumber = num -> {
			if (num == 0 || num == 1)
				return false;

			for (int i = 2; i <= Math.sqrt(num); i++) {
				if (num % i == 0) {
					return false;
				}
			}

			return true;
		};
		Set<Integer> setSieveOfEratosthenes = new HashSet<Integer>();
		for (int i = 2; i <= sieveMax; i++)
			setSieveOfEratosthenes.add(i);
		for (int i = 2; i <= Math.sqrt(sieveMax); i++) {
			if (isPrimeNumber.test(i))
				for (int j = 2; i * j <= sieveMax; j++)
					if (setSieveOfEratosthenes.contains(i * j))
						setSieveOfEratosthenes.remove(i * j);
		}

		// PRINT
		for (int tc : arrTestCase) {
			int goldbachPartition = 0;
			for (int i = 2; i <= tc / 2; i++) {
				if (setSieveOfEratosthenes.contains(i) && setSieveOfEratosthenes.contains(tc - i))
					goldbachPartition++;
			}
			sb.append(goldbachPartition).append("\n");
		}
		System.out.println(sb);

	}

}