import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, numbers
		int size = Integer.parseInt(br.readLine());
		int[] nums = new int[size];
		{
			StringTokenizer st = new StringTokenizer(br.readLine());
			int i = 0;
			while (st.hasMoreTokens())
				nums[i++] = Integer.parseInt(st.nextToken());
		}

		// INIT kadanes sub set
		TreeSet<Integer> setKadanes = new TreeSet<Integer>();
		int subsum = nums[0];
		setKadanes.add(subsum);
		for (int i = 1; i < size; i++) {
			subsum = Math.max(subsum + nums[i], nums[i]);
			setKadanes.add(subsum);
		}

		// PRINT
		System.out.println(setKadanes.last());
		
	}

}