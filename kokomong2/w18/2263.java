import java.io.*;
import java.util.*;

public class Main {
	static int [] in, post, pre;
	static int index = 0;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		in = new int[n];
		post = new int[n];
		pre = new int[n];
		for (int i = 0; i < n; i++) {
			in[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			post[i] = Integer.parseInt(st.nextToken());
		}
		getPreOrder(0, n - 1, 0, n - 1);
		for (int i = 0; i < n; i++) {
			bw.write(pre[i] + " ");
		}
		bw.flush();
		bw.close();
	}

	public static void getPreOrder (int is, int ie, int ps, int pe) {

		if (is <= ie && ps <= pe) {
			pre[index++] = post[pe];

			int pos = is;
			for (int i = is; i <= ie; i++) {
				if (in[i] == post[pe]){
					pos = i;
					break;
				}
			}

			getPreOrder(is, pos - 1, ps, ps + (pos - is) - 1);
			getPreOrder(pos + 1, ie, ps + (pos - is), pe - 1);
		}
	}
}
