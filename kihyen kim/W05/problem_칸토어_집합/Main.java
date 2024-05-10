import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT cantor lamda function
		Function<Integer, Boolean[]> funcGenerateCantorSet = new Function<Integer, Boolean[]>() {

			@Override
			public Boolean[] apply(Integer size) {
				Boolean[] arrCantorSet = new Boolean[size];
				Arrays.fill(arrCantorSet, true);
				
				cantor(arrCantorSet, 0, arrCantorSet.length-1);
				return arrCantorSet;
			}
			
			public void cantor(Boolean[] arr, Integer idxStart, Integer idxEnd) {
				int len = (idxEnd+1 - idxStart) / 3;
				if (len > 0) {
					// recursion index between 0/3 to 1/3
					cantor(arr, idxStart, idxStart + len - 1);

					// recursion index between 2/3 to 3/3
					cantor(arr, idxStart + (len*2), idxEnd);
					
					// kill index between 1/3 to 2/3
					for (int i = idxStart + len; i <= idxEnd - len; i++)
						arr[i] = false;
				}
			}
		};

		// RUN
		String str;
		while ((str = br.readLine()) != null)
		{
			// INIT
			int size = (int)Math.pow(3, Integer.parseInt(str));

			// GENERATE
			sb = new StringBuilder();
			for(boolean b : funcGenerateCantorSet.apply(size))
				sb.append(b ? "-" : " ");

			// PRINT
			System.out.println(sb);
		}

	}

}