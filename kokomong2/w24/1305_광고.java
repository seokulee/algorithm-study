
import java.io.*;

public class Main {


	static int[] pi;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int length = Integer.parseInt(br.readLine());
		String P = br.readLine();

		pi = new int[P.length()];

		getPI(P);
		bw.write(length - pi[P.length() - 1] + "\n");

		bw.flush();
		bw.close();
		br.close();
	}


	static void getPI(String p) {
		int j = 0;
		for (int i = 1; i < p.length(); i++) {
			while (j > 0 && p.charAt(i) != p.charAt(j))
				j = pi[j - 1];
			if (p.charAt(i) == p.charAt(j)) {
				pi[i] = ++j;
			} else {
				pi[i] = 0;
			}
		}
	}
}
