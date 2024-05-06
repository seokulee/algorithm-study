import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size
		String[] nums = br.readLine().split(" ");
		int size = Integer.parseInt(nums[0]);
		int execution = Integer.parseInt(nums[1]);
		List<Integer> list = new ArrayList<Integer>();
		for(int i=1; i<=size; i++)
			list.add(i);

		// CLAC josephus permutation
		int index = execution-1;
		while(true) {
			sb.append(list.remove(index));
			
			if(list.size() == 0)
				break;
			else
				sb.append(", ");
			
			index = (index-1 + execution) % list.size();
		}

		// PRINT
		System.out.println("<" + sb + ">");

	}

}