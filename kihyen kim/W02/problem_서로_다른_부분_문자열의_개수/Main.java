import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;



public class Main {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		// INIT str, str subset
		String str = br.readLine();
		Set<String> setStrSubset = new HashSet<String>();
		for(int i=1; i<=str.length(); i++) {
			for(int j=0; j<=str.length()-i; j++) {
				String strSubset = str.substring(j,j+i);
				if (!setStrSubset.contains(strSubset))
					setStrSubset.add(strSubset);
			}			
		}
		
		// PRINT
		System.out.println( sb.append(setStrSubset.size()) );

	}

}