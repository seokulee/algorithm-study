import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.function.Supplier;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		// INIT size, required count
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int required = Integer.parseInt(st.nextToken());
		
		// INIT array of cables
		long[] arrCables = new long[size];
		for (int i=0; i<size; i++)
			arrCables[i] = Long.parseLong(br.readLine());
		Arrays.sort(arrCables);

		// INIT lambda function
		Supplier<Object> funcParametricSearch = new Supplier<Object>() {
			
			long result;

			@Override
			public Object get() {
				parametricSearch(1, arrCables[arrCables.length-1]);
				return result;
			}
			
			void parametricSearch(long min, long max) {
				if (min > max) {
					result = max;
					return;
				}
				
				long mid = (min + max) / 2;
				
				int cntCable = 0;
				for (long cable : arrCables)
					cntCable += cable / mid;
				
				if (cntCable < required)
					parametricSearch(min, mid-1);
				else
					parametricSearch(mid+1, max);
			}
			
		};

		// PRINT
		System.out.println( (long)funcParametricSearch.get() );

	}

}