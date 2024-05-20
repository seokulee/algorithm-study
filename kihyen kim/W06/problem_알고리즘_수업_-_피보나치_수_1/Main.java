import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT num
		int num = Integer.parseInt(br.readLine());

		// INIT function fibonacci by recursion
		Function<Integer, Integer> funcRecursion = new Function<Integer, Integer>() {
			
			int cntRun = 1;
			
			@Override
			public Integer apply(Integer num) {
				fibonacci(num);
				
				return cntRun;
			}
			int fibonacci(Integer num) {
				if (num == 1 || num == 2)
					return 1;
				
				cntRun++;
				
				return (fibonacci(num - 1) + fibonacci(num - 2));
			}
		};

		// INIT function fibonacci by dynamic programming
		Function<Integer, Integer> funcDynamicProgramming = new Function<Integer, Integer>() {

			int cntRun = 0;
			int[] fibonacci;

			@Override
			public Integer apply(Integer num) {
				fibonacci = new int[num];
				fibonacci(num);

				return cntRun;
			}
			int fibonacci(Integer num) {
				fibonacci[0] = fibonacci[1] = 1;
				
				for (int i = 2; i < num; i++, cntRun++)
					fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];

				return fibonacci[num - 1];
			}
		};

		// PRINT
		sb
			.append(funcRecursion.apply(num))
			.append(" ")
			.append(funcDynamicProgramming.apply(num));
		System.out.println(sb);
		
	}

}