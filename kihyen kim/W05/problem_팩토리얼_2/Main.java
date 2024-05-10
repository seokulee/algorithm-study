import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT number
		int num = Integer.parseInt(br.readLine());

		// INIT factorial lamda function
		Function<Integer, Long> funcFactorial = new Function<Integer, Long>() {
			@Override
			public Long apply(Integer n)
			{
				return 	(n == 0) ? 	1 :
						(n > 1)  ? 	n*apply(n - 1) :
									n;
			}
		};

		// PRINT
		System.out.println(funcFactorial.apply(num));

	}

}