import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT number
		int num = Integer.parseInt(br.readLine());

		// INIT fibonacci lamda function
		Function<Integer, Long> funcFibonacci = new Function<Integer, Long>() {
			@Override
			public Long apply(Integer n)
			{
				return 	(n == 0) ? 	0 :
						(n == 1) ? 	1 :
									apply(n-2) + apply(n-1);
			}
		};

		// PRINT
		System.out.println(funcFibonacci.apply(num));

	}

}