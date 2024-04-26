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
		Map<Integer, Integer> mapNumbers = new HashMap<Integer, Integer>();
		{
			String[] numbers = br.readLine().split(" ");
			for(String num : numbers)
				if(!mapNumbers.containsKey(Integer.parseInt(num)))
					mapNumbers.put(Integer.parseInt(num), 1);
				else
					mapNumbers.put(Integer.parseInt(num), mapNumbers.get(Integer.parseInt(num))+1);
		}

		// INIT matchers
		br.readLine(); // SKIP size of matchers
		String[] matchers = br.readLine().split(" ");
	
		// PRINT
		for(String match : matchers) {
			if(!mapNumbers.containsKey(Integer.parseInt(match)))
				sb.append("0 ");
			else
				sb.append(mapNumbers.get(Integer.parseInt(match))).append(' ');
		}
		System.out.println(sb);

	}

}