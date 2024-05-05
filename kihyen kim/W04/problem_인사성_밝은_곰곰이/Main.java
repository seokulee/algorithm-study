import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, greeted count
		int size = Integer.parseInt(br.readLine());
		int cntGreeted = 0;

		// CALC greeted count
		Set<String> setGreeted = new HashSet<String>();
		for (int i = 0; i < size; i++)
		{
			String log = br.readLine();
			if (log.equals("ENTER")) {
				cntGreeted += setGreeted.size();
				setGreeted.clear();
			}
			else
				setGreeted.add(log);
		}
		cntGreeted += setGreeted.size();

		// PRINT
		System.out.println(cntGreeted);

	}

}