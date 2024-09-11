import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[] parent;
    static int[] visited;
    static ArrayList<Integer>[] map;
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        parent = new int[n + 1];
        visited = new int[n + 1];
        map = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++)
            map[i] = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            map[a].add(b);
            map[b].add(a);
        }
        dfs(1);
        for (int i = 2; i <= n; i++)
            System.out.println(parent[i]);
    }

    public static void dfs(int now)
    {
        for(int i : map[now]){
            if (visited[i] == 0){
                visited[i] = 1;
                parent[i] = now;
                dfs(i);
            }
        }
    }
}