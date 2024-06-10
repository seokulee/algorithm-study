import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.function.Function;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		// INIT size, exponent, matrix
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		long exponent = Long.parseLong(st.nextToken());
		long[][] baseMatrix = new long[size][size];
		for (int i = 0; i < size; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < size; j++)
				baseMatrix[i][j] = Integer.parseInt(st.nextToken());
		}

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
		long[][] result = (long[][]) funcCalcMatrixPowerAndMod.apply(new Object[] {baseMatrix, exponent, (long)1000});

		// PRINT
		for (long[] row : result) {
			for (long num : row)
				sb.append(num).append(" ");
			sb.append("\n");
		}
		System.out.println(sb);

	}

}