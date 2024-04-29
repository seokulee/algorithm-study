import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;



public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// INIT sizes
		String[] sizes = br.readLine().split(" ");
		int sizeMySet = Integer.parseInt(sizes[0]);
		int sizeMatchers = Integer.parseInt(sizes[1]);
		
		// INIT my set
		Map<String, Boolean> mapMySet = new HashMap<String, Boolean>();
		for(int i=0; i<sizeMySet; i++)
			mapMySet.put(br.readLine(), true);
	
		// PRINT
		int matched = 0;
		for(int i=0; i<sizeMatchers; i++) {
			if(mapMySet.containsKey(br.readLine()))
				matched++;
		}
		System.out.println(matched);

	}

}