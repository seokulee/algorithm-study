import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.function.Supplier;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT base, exponent, divisor
		st = new StringTokenizer(br.readLine());
		long base = Integer.parseInt(st.nextToken());
		int exponent = Integer.parseInt(st.nextToken());
		int divisor = Integer.parseInt(st.nextToken());

		// INIT lamda function
		Supplier<Long> funcGeneratePowerAndMod = new Supplier<Long>() {

			@Override
			public Long get() {
				return recursion(base, exponent);
			}

			public long recursion(long base, int exponent) {
				if (exponent == 1)
					return base % divisor;

				long pow = recursion(base, exponent / 2);

				if ((exponent & 1) == 1)
					return (pow * pow % divisor) * base % divisor;
				else
					return pow * pow % divisor;
			}

		};

		// CALC & PRINT
		System.out.println( funcGeneratePowerAndMod.get() );

	}

}