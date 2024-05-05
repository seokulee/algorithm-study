import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT num
		int num = Integer.parseInt(br.readLine());
		
		int result = 1;
		for(int i=num; i>1; i--)
			result *= i;

		// PRINT
		System.out.println(result);

	}

}