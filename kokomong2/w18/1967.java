import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static ArrayList<Node>[] tree;
    static int[] visited;
    static int max, last;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        tree = new ArrayList[n + 1];
        visited = new int[n + 1];
        for (int i = 0; i <= n; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int now = Integer.parseInt(st.nextToken());
            int next = Integer.parseInt(st.nextToken());
            int len = Integer.parseInt(st.nextToken());
            tree[now].add(new Node(next, len));
            tree[next].add(new Node(now, len));
        }
        max = 0;
        visited[1] = 1;
        dfs(0, 1);
        visited = new int[n + 1];
        visited[last] = 1;
        dfs(0, last);
        System.out.println(max);
    }

    public static void dfs(int len, int now){
        if (len > max){
            max = len;
            last = now;
        }
        for(Node node : tree[now]){
            if (visited[node.next] == 0){
                visited[node.next] = 1;
                dfs(len + node.len, node.next);
            }
        }
    }
}

class Node {
    int next;
    int len;

    public Node(int next, int len) {
        this.next = next;
        this.len = len;
    }
}
