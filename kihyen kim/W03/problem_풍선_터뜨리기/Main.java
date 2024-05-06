import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, balloon list
		int size = Integer.parseInt(br.readLine());
		List<Integer[]> listBalloon = new ArrayList<Integer[]>();
		String[] nums = br.readLine().split(" ");
		for(int i=0; i<size; i++)
			listBalloon.add( new Integer[]{ i+1, Integer.parseInt(nums[i]) } );

		// RUN
		int index = 0;
		int execution;
		while(true) {
			sb.append( listBalloon.get(index)[0] ).append(" ");
			execution = listBalloon.remove(index)[1];
			
			if (listBalloon.isEmpty())
				break;
			
			index = (index-1 + (execution<0 ? execution+1 : execution)) % listBalloon.size();
			if (index < 0)
				index += listBalloon.size();
		}

		// PRINT
		System.out.println(sb);

	}

}