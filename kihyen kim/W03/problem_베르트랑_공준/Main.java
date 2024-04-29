import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.Predicate;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT test cases, max num
		List<Integer> listTestCase = new ArrayList<Integer>();
		int sieveMax = 0;
		while (true) {
			String str = br.readLine();
			if (str.equals("0"))
				break;

			int num = Integer.parseInt(str);
			listTestCase.add(num);
			if (num > sieveMax)
				sieveMax = num;
		}
		sieveMax *= 2;

		// INIT sieve of eratosthenes
		Set<Integer> setSieveOfEratosthenes = new TreeSet<Integer>();
		for (int i = 2; i <= sieveMax; i++)
			setSieveOfEratosthenes.add(i);

		// CALC by sieve of eratosthenes
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
		for (int i = 2; i <= Math.sqrt(sieveMax); i++) {
			if (isPrimeNumber.test(i))
				for (int j = 2; i * j <= sieveMax; j++)
					if (setSieveOfEratosthenes.contains(i * j))
						setSieveOfEratosthenes.remove(i * j);
		}

		// PRINT
		for (int tc : listTestCase) {
			Set<Integer> setRange = new TreeSet<Integer>();
			for (int i = tc + 1; i <= tc * 2; i++)
				setRange.add(i);

			setRange.retainAll(setSieveOfEratosthenes);
			sb.append(setRange.size()).append("\n");
		}
		System.out.println(sb);

	}

}