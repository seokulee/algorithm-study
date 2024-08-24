import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

	static List<Integer> comList1 = new ArrayList<>();
	static List<Integer> comList2 = new ArrayList<>();
	static int N, C;
	static int[] arr;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		comb(comList1, 0, N / 2, 0);
		comb(comList2, N / 2 , N, 0);
		Collections.sort(comList2);

		int cnt = 0;
		for (int left : comList1) {
			cnt += bs(0, comList2.size() - 1, left) + 1;
		}
		System.out.println(cnt);
	}

	public static int bs (int start, int end, int val) {
		int mid;
		while (start <= end) {
			mid = (start + end) / 2;
			if (comList2.get(mid) <= C - val) {
				start = mid + 1;
			} else {
				end = mid - 1;
			}
		}
		return end;
	}

	public static void comb (List<Integer> lst, int start, int end, int sum) {
		if (sum > C)
			return;
		if (start == end) {
			lst.add(sum);
			return;
		}

		comb(lst, start + 1, end, sum);
		comb(lst, start + 1, end, sum + arr[start]);
	}
}
