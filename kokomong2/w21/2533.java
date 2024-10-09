import java.io.*;
import java.util.*;

public class Main {

    static ArrayList<Integer>[] tree;
    static int[][] dp;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        tree = new ArrayList[N + 1];
        dp = new int[N + 1][2];
        visited = new boolean[N + 1];

        for (int i = 1; i <= N; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            tree[u].add(v);
            tree[v].add(u);
        }

        dfs(1);

        System.out.println(Math.min(dp[1][0], dp[1][1]));
    }

    static void dfs(int node) {
        visited[node] = true;
        dp[node][0] = 0; // 얼리 어답터가 아닌 경우
        dp[node][1] = 1; // 얼리 어답터인 경우 (자기 자신)

        for (int child : tree[node]) {
            if (!visited[child]) {
                dfs(child);
                dp[node][0] += dp[child][1];
                dp[node][1] += Math.min(dp[child][0], dp[child][1]);  // 현재 노드가 얼리 어답터인 경우, 자식은 얼리 어답터일 수도 아닐 수도 있음
            }
        }
    }
}
