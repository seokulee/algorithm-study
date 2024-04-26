import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;



public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		// SKIP sizes
		br.readLine();
		
		// INIT elements
		Set<Integer> setA = new HashSet<Integer>();
		for(String s : br.readLine().split(" ")) {
			int element = Integer.parseInt(s);
			setA.add(element);	
		}
	
		// PRINT
		int differenceB = 0;
		for(String s : br.readLine().split(" ")) {
			int element = Integer.parseInt(s);
			if (setA.contains(element))
				setA.remove(element);
			else
				differenceB++;
		}
		int differenceA = setA.size();
		System.out.println( sb.append(differenceA + differenceB) );

	}

}