import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT exponent
		long exponent = Long.parseLong(br.readLine());

		// INIT lambda function
		Function<Object[], Object> funcCalcMatrixPowerAndMod = new Function<Object[], Object>() {
			
			long[][] base;
			int size;
			long divisor;
			
			@Override
			public Object apply(Object[] params) {
				this.base = (long[][])params[0];
				this.size = base.length;
				long exponent = (long)params[1];
				this.divisor = (long)params[2];
				
				return recursion(exponent);
			}

			public long[][] recursion(long exponent) {
				if (exponent == 1L) {
					for (int i = 0; i < size; i++)
						for (int j = 0; j < size; j++)
							base[i][j] %= divisor;
					return base;
				}
				
				long[][] pow = recursion(exponent / 2);
				
				long[][] result1 = new long[size][size];
				for (int i = 0; i < size; i++) {
					for (int j = 0; j < size; j++) {
						long sum = 0;
						for (int k = 0; k < size; k++)
							sum += (pow[i][k] * pow[k][j] % divisor);
						
						result1[i][j] = sum % divisor;
					}
				}
				
				if ((exponent & 1) == 0)
					return result1;
				
				long[][] result2 = new long[size][size];
				for (int i = 0; i < size; i++) {
					for (int j = 0; j < size; j++) {
						long sum = 0;
						for (int k = 0; k < size; k++)
							sum += (result1[i][k] * base[k][j] % divisor);
						
						result2[i][j] = sum % divisor;
					}
				}
				
				return result2;
			}
			
		};
		
		// CALC
		/*		| 1  1 |^x-1 | F(1) |   |  F(x)  |
				|      |   * |      | = |        |
				| 1  0 |     | F(0) |   | F(x-1) |, but A[0][0] not changes by multiplier
		 */
		long[][] baseMatrix = new long[][]
				{
					{1, 1} ,
					{1, 0}
				};
		long result = (exponent == 1L) ? 1 : ((long[][]) funcCalcMatrixPowerAndMod.apply(new Object[] {baseMatrix, exponent-1, (long)1000000007}))[0][0];
		
		// PRINT
		System.out.println(result);

	}

}