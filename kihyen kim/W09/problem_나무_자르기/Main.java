import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.function.Supplier;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		// INIT size, required length
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int required = Integer.parseInt(st.nextToken());
		
		// INIT array of trees
		int[] arrTrees = new int[size];
		st = new StringTokenizer(br.readLine());
		for (int i=0; i<size; i++)
			arrTrees[i] = Integer.parseInt(st.nextToken());
		Arrays.sort(arrTrees);

		// INIT lambda function
		Supplier<Object> funcParametricSearch = new Supplier<Object>() {
			
			long result;

			@Override
			public Object get() {
				parametricSearch(1, arrTrees[arrTrees.length-1]);
				return result;
			}
			
			void parametricSearch(int min, int max) {
				if (min > max) {
					result = max;
					return;
				}
				
				int mid = (min + max) / 2;
				
				long lenLog = 0;
				for (int tree : arrTrees)
					lenLog += (tree > mid) ? tree - mid : 0;
				
				if (lenLog < required)
					parametricSearch(min, mid-1);
				else
					parametricSearch(mid+1, max);
			}
			
		};

		// PRINT
		System.out.println( (long)funcParametricSearch.get() );

	}

}