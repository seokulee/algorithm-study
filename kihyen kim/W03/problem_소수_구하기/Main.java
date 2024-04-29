import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Set;
import java.util.TreeSet;
import java.util.function.Predicate;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT first num, last num
		String[] nums = br.readLine().split(" ");
		int firstNum = Integer.parseInt(nums[0]);
		int lastNum = Integer.parseInt(nums[1]);

		// INIT sieve of eratosthenes
		Set<Integer> setSieveOfEratosthenes = new TreeSet<Integer>();
		for (int i = (firstNum > 2) ? firstNum : 2; i <= lastNum; i++)
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
		for (int i = 2; i <= Math.sqrt(lastNum); i++) {
			if (isPrimeNumber.test(i))
				for (int j = 2; i*j <= lastNum; j++)
					if (setSieveOfEratosthenes.contains(i * j))
						setSieveOfEratosthenes.remove(i * j);
		}

		// PRINT
		for (int num : setSieveOfEratosthenes)
			sb.append(num).append("\n");
		System.out.println(sb);

	}

}