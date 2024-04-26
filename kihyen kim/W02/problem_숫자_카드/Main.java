import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;



public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		// INIT numbers
		br.readLine(); // SKIP size of numbers
		Map<Integer, Boolean> mapNumbers = new HashMap<Integer, Boolean>();
		{
			String[] numbers = br.readLine().split(" ");
			for(String num : numbers)
				mapNumbers.put(Integer.parseInt(num), true);
		}

		// INIT matchers
		br.readLine(); // SKIP size of matchers
		String[] matchers = br.readLine().split(" ");
	
		// PRINT
		for(String match : matchers) {
			if(mapNumbers.containsKey(Integer.parseInt(match)))
				sb.append("1 ");
			else
				sb.append("0 ");
		}
		System.out.println(sb);

	}

}