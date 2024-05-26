import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, sequence
		int size = Integer.parseInt(br.readLine());
		int[] arrSequence = new int[size];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < size; i++)
			arrSequence[i] = Integer.parseInt(st.nextToken());

		// INIT dynamic programming array x2
		int[] dpForward = new int[size];
		dpForward[0] = 1;
		for (int i = 1; i < size; i++)
		{
			int maxLISBefore = 0;
			for (int j = 0; j < i; j++) {
				if (arrSequence[j] < arrSequence[i])
					maxLISBefore = (dpForward[j] > maxLISBefore) ? dpForward[j] : maxLISBefore;
			}
			dpForward[i] = maxLISBefore + 1;
		}
		int[] dpReverse = new int[size];
		dpReverse[size-1] = 1;
		for (int i = size-1; i >= 0; i--)
		{
			int maxLISBefore = 0;
			for (int j = size-1; j > i; j--) {
				if (arrSequence[j] < arrSequence[i])
					maxLISBefore = (dpReverse[j] > maxLISBefore) ? dpReverse[j] : maxLISBefore;
			}
			dpReverse[i] = maxLISBefore + 1;
		}

		// CALC & PRINT
		int maxBitonicLen = 0;
		for (int i = 0; i < size; i++) {
			int lenBitonic = dpForward[i] + dpReverse[i] - 1;
			maxBitonicLen = (lenBitonic > maxBitonicLen) ? lenBitonic : maxBitonicLen;
		}
		System.out.println(maxBitonicLen);
		
	}

}