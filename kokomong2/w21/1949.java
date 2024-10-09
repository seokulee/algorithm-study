import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[] population;
    static ArrayList<Integer>[] tree;
    static boolean[] visited;
    static int[][] dp;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        population = new int[N + 1];
        tree = new ArrayList[N + 1];
        visited = new boolean[N + 1];
        dp = new int[N + 1][2];               // DP 테이블, [마을][우수 마을 여부]

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            population[i] = Integer.parseInt(st.nextToken());
            tree[i] = new ArrayList<>();
        }

        for (int i = 0; i < N - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            tree[u].add(v);
            tree[v].add(u);
        }

        dfs(1);

        System.out.println(Math.max(dp[1][0], dp[1][1]));
    }

    static void dfs(int node) {
        visited[node] = true;

        dp[node][1] = population[node];

        for (int neighbor : tree[node]) {
            if (!visited[neighbor]) {
                dfs(neighbor);

                dp[node][0] += Math.max(dp[neighbor][0], dp[neighbor][1]);
                dp[node][1] += dp[neighbor][0];
            }
        }
    }
}
