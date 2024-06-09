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
		long[] arr = new long[size];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<size; i++)
			arr[i] = Long.parseLong(st.nextToken());
		Arrays.sort(arr);

		// INIT lambda function
		Function<Object[], Object> funcBinarySearch = new Function<Object[], Object>() {
			
			long target;
			
			@Override
			public Object apply(Object[] params) {
				this.target = (long)params[0];
				
				return binarySearch(arr.length-1, 0);
			}
			
			boolean binarySearch(int idxTop, int idxBtm) {
				if (idxBtm > idxTop)
					return false;
				
				int idxMid = (idxBtm + idxTop) / 2;

				if (target == arr[idxMid]) // found
					return true;
				
				if (target < arr[idxMid])
					return binarySearch(idxMid-1, idxBtm);
				else
					return binarySearch(idxTop, idxMid+1);
			}

		};

		// PRINT
		br.readLine(); // SKIP size
		st = new StringTokenizer(br.readLine());
		while(st.hasMoreTokens()) {
			long target = Long.parseLong(st.nextToken());
			sb.append( ( (boolean)funcBinarySearch.apply(new Object[] {target}) ) ? "1\n" : "0\n" );
		}
		System.out.println(sb);

	}

}