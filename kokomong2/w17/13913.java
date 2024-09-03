import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
	static int N, K;
	static int[] arr;
	static boolean[] visited;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		arr = new int[100001];
		visited = new boolean[100001];
		fillArray();
		fillArray();
		
		int index = K;
		StringBuilder sb =  new StringBuilder();
		sb.append(arr[K]).append("\n");
		Stack<Integer> stack = new Stack<>();
		stack.add(index);
		while (index != N) {
			if (index / 2 > 0 && index % 2 == 0 && arr[index / 2] == arr[index] - 1) {
				index = index / 2;
				stack.add(index);
			} else if (index - 1 >= 0 && arr[index - 1] == arr[index] - 1 ) {
				index = index - 1;
				stack.add(index);
			} else if (index + 1 <= 100000 && arr[index + 1] == arr[index] - 1) {
				index = index + 1;
				stack.add(index);
			} else {
				break;
			}
		}
		while (!stack.isEmpty()) {
			sb.append(stack.pop()).append(" ");
		}
		System.out.println(sb);
	}

	public static void fillArray() {
		PriorityQueue<Integer> pq = new PriorityQueue<>();
		Arrays.fill(visited, false);
		pq.add(N);
		while (!pq.isEmpty()) {
			int now = pq.poll();
			if (visited[now])
				continue;
			visited[now] = true;
			if (now < 100000 && now + 1 != N) {
				arr[now + 1] = arr[now + 1] == 0 ? arr[now] + 1 : Math.min(arr[now + 1], arr[now] + 1);
				pq.add(now + 1);
			}
			if (now > 0 && now - 1 != N){
				arr[now - 1] = arr[now - 1] == 0 ? arr[now] + 1 : Math.min(arr[now - 1], arr[now] + 1);
				pq.add(now - 1);
			}
			if (now <= 50000 && now * 2 != N) {
				arr[now * 2] = arr[now * 2] == 0 ? arr[now] + 1 : Math.min(arr[now * 2], arr[now] + 1);
				pq.add(now * 2);
			}
		}
	}

}

