import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.function.Function;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		// INIT array
		int size = Integer.parseInt(br.readLine());
		int[] arr = new int[size];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < size; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		Arrays.sort(arr);

		// INIT lambda function
		Function<Object[], Object> funcBinarySearch = new Function<Object[], Object>() {
			
			int target;
			
			@Override
			public Object apply(Object[] params) {
				this.target = (int)params[0];
				
				return searchUpperBound(0, arr.length-1) - searchLowerBound(0, arr.length-1);
			}
			
			int searchLowerBound(int idxBtm, int idxTop) {
				if (idxBtm > idxTop)
					return idxBtm;
				
				int idxMid = (idxBtm + idxTop) / 2;
				
				if (target <= arr[idxMid])
					return searchLowerBound(idxBtm, idxMid-1);
				else
					return searchLowerBound(idxMid+1, idxTop);
			}
			int searchUpperBound(int idxBtm, int idxTop) {
				if (idxBtm > idxTop)
					return idxBtm;
				
				int idxMid = (idxBtm + idxTop) / 2;
				
				if (target >= arr[idxMid])
					return searchUpperBound(idxMid+1, idxTop);
				else
					return searchUpperBound(idxBtm, idxMid-1);
			}
			
		};

		// PRINT
		br.readLine(); // SKIP size
		st = new StringTokenizer(br.readLine());
		while(st.hasMoreTokens()) {
			int target = Integer.parseInt(st.nextToken());
			sb.append( (int)funcBinarySearch.apply(new Object[] {target}) ).append(" ");
		}
		System.out.println(sb);

	}

}



/*
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
*/