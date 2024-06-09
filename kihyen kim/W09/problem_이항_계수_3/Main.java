import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.function.Function;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT numbers, divisor
		st = new StringTokenizer(br.readLine());
		long numN = Long.parseLong(st.nextToken());
		long numK = Long.parseLong(st.nextToken());
		long divisor = 1000000007;

		// INIT lambda function
		Function<Object[], Object> funcGeneratePowerAndMod = new Function<Object[], Object>() {

			@Override
			public Object apply(Object[] params) {
				long base = (long)params[0];
				long exponent = (long)params[1];
				long divisor = (long)params[2];
				
				return recursion(base, exponent, divisor);
			}

			public long recursion(long base, long exponent, long divisor) {
				if (exponent == 1L)
					return base % divisor;

				long pow = recursion(base, exponent / 2, divisor);

				if ((exponent & 1) == 1)
					return (pow * pow % divisor) * base % divisor;
				else
					return pow * pow % divisor;
			}

		};
		
		// CALC factorial N!
		long mulA = 1; // N!
		for (long i = numN; i >= 1; i--)
			mulA = mulA * i % divisor;
		
		// CALC factorial K!(N-K)!
		long mulB = 1; // K!(N-K)!
		for (long i = numK; i >= 1; i--)
			mulB = mulB * i % divisor;
		for (long i = numN - numK; i >= 1; i--)
			mulB = mulB * i % divisor;
		
		// CALC (K!(N-K)!)^p-2
		mulB = (long) funcGeneratePowerAndMod.apply(new Object[] {mulB, divisor-2, divisor});
		
		// PRINT
		System.out.println( mulA * mulB % divisor );

	}

}