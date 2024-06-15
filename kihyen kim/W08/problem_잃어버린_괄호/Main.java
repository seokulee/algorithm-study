import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT array of split by minus
		String[] arrSubtraction = br.readLine().split("[-]");

		// CALC
		int result = 0;
		for (int i=0; i<arrSubtraction.length; i++) {
			String[] arrAddition = arrSubtraction[i].split("[+]");
			int sum = 0;
			for (String num : arrAddition)
				sum += Integer.parseInt(num);
			
			if (i == 0)
				result += sum;
			else
				result -= sum;
		}
		
		// PRINT
		System.out.println(result);

	}

}