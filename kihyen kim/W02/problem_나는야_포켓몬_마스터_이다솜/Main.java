import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;



public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		// INIT sizes
		String[] sizes = br.readLine().split(" ");
		int sizePokedex = Integer.parseInt(sizes[0]);
		int sizeProblem = Integer.parseInt(sizes[1]);
		
		// INIT pokedex
		List<String> listPokedex = new ArrayList<>();
		Map<String, Integer> mapPokedex = new HashMap<>();
		for(int i=0; i<sizePokedex; i++) {
			String name = br.readLine();
			
			listPokedex.add(name);
			mapPokedex.put(name, i+1);
		}
		
		// PRINT
		for(int i=0; i<sizeProblem; i++) {
			String problem = br.readLine();
			if(48 <= problem.charAt(0) && problem.charAt(0) <= 57) // if problem number?
				sb.append(listPokedex.get(Integer.parseInt(problem)-1)).append('\n');
			else
				sb.append(mapPokedex.get(problem)).append('\n');
		}
		System.out.println(sb);

	}

}