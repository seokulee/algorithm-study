import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT num
		int num = Integer.parseInt(br.readLine());

		// PRINT
		System.out.println(num * (num - 1));

	}

}