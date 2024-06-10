import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.function.Supplier;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		
		// INIT size, count of router, array of location
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int cntRouter = Integer.parseInt(st.nextToken());
		int[] arrLocation = new int[size];
		for (int i = 0; i < size; i++)
			arrLocation[i] = Integer.parseInt(br.readLine());
		Arrays.sort(arrLocation);

		// INIT lambda function
		Supplier<Object> funcBinarySearch = new Supplier<Object>() {
			
			int result;
			
			@Override
			public Object get() {
				searchUpperBound(1, arrLocation[arrLocation.length-1] - arrLocation[0]);
				
				return result;
			}
			
			void searchUpperBound(int idxBtm, int idxTop) {
				if (idxBtm > idxTop)
					return;
				
				int idxMid = (idxBtm + idxTop) / 2;
				int cntInstallable = 1;
				{
					int lastestLocate = arrLocation[0];

					for (int i = 1; i < arrLocation.length; i++) {
						int locate = arrLocation[i];
						if (locate - lastestLocate >= idxMid) {
							cntInstallable++;
							lastestLocate = locate;
						}
					}
				}

				if (cntInstallable < cntRouter)
					searchUpperBound(idxBtm, idxMid-1);
				else {
					result = idxMid;
					searchUpperBound(idxMid + 1, idxTop);
				}
			}
			
		};

		// PRINT
		System.out.println( (int)funcBinarySearch.get() );

	}

}