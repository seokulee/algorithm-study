import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.function.Consumer;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, list of longest increasing subsequence
		int size = Integer.parseInt(br.readLine());
		List<Integer> listLIS = new ArrayList<>();

		// INIT lambda function
		Consumer<Object> funcSearchNearestIndexAndInsert = new Consumer<Object>() {

			int target;

			@Override
			public void accept(Object param) {
				this.target = (int) param;
				
				listLIS.set(searchNearestIndex(0, listLIS.size()-1), target);
			}

			int searchNearestIndex(int idxLeft, int idxRight) {
				if (idxLeft >= idxRight)
					return idxLeft;

				int idxMid = (idxLeft + idxRight) / 2;

				if (target > listLIS.get(idxMid))
					return searchNearestIndex(idxMid+1, idxRight); // modify the range exclude mid
				else
					return searchNearestIndex(idxLeft, idxMid); // modify the range include mid
			}
			
		};

		// CALC
		st = new StringTokenizer(br.readLine());
		listLIS.add(Integer.parseInt(st.nextToken()));
		while(st.hasMoreTokens()) {
			int num = Integer.parseInt(st.nextToken());

			if (num > listLIS.get(listLIS.size()-1))
				listLIS.add(num);
			else
				funcSearchNearestIndexAndInsert.accept(num);
		}

		// PRINT
		System.out.println(listLIS.size());

	}

}