import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT num
		int num = Integer.parseInt(br.readLine());
		
		// CALC opened num
		int numOpened = 1; // except first window
		for (int i = 2; i*i <= num; i++)
			numOpened++;

		// PRINT
		System.out.println(numOpened);

	}

}