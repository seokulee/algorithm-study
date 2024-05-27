import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;

		// INIT string, count of test case
		char[] str = br.readLine().toCharArray();
		int cntTestCase = Integer.parseInt(br.readLine());

		// INIT dynamic programming array
		int[][] dpCnt = new int[60][str.length];
		for (int i = 0; i < str.length; i++) {
			char ch = str[i];
			
			for (int j = 0; j < 60; j++) {
				int cntLatest = (i==0) ? 0 : dpCnt[j][i-1];
				if (j == ch-'A')
					dpCnt[j][i] = cntLatest+1;
				else
					dpCnt[j][i] = cntLatest;
			}
		}

		// CALC
		for (int i = 0; i < cntTestCase; i++) {
			st = new StringTokenizer(br.readLine());
			char ch = st.nextToken().charAt(0);
			int idxExclude = Integer.parseInt(st.nextToken()) -1;
			int idxEndOfRange = Integer.parseInt(st.nextToken());
			
			int value = dpCnt[ch-'A'][idxEndOfRange] - ((idxExclude < 0) ? 0 : dpCnt[ch-'A'][idxExclude]);
			sb.append(value).append("\n");
		}
		
		// PRINT
		System.out.println(sb);

	}

}