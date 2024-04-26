import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;



public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		// INIT sizes
		String[] sizes = br.readLine().split(" ");
		int sizeRoster = Integer.parseInt(sizes[0]);
		int sizeMatchers = Integer.parseInt(sizes[1]);
		
		// INIT roster
		Set<String> setRoster = new HashSet<String>();
		for(int i=0; i<sizeRoster; i++) {
			String name = br.readLine();
			setRoster.add(name);
		}
		
		// INIT matched roster
		Set<String> setMatchedRoster = new TreeSet<String>();
		for(int i=0; i<sizeMatchers; i++) {
			String name = br.readLine();
			if (setRoster.contains(name))
				setMatchedRoster.add(name);
		}
	
		// PRINT
		sb.append(setMatchedRoster.size()).append('\n');
		for (String name : setMatchedRoster) {
			sb.append(name).append('\n');
		}
		System.out.println(sb);

	}

}