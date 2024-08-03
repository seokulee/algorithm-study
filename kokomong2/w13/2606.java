import java.util.*;


public class Main {

    static int[] visited;
    static int N;
    static int M;
    static int V;
    static int cnt = 0;
    static ArrayList<Integer>[] list;

    static void DFS(int start){
        for (int end : list[start]) {
            int next = end;
            if(visited[next] ==0 ){
                visited[next]=1;
                cnt++;
                DFS(next);
            }
        }

    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        list = new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            list[start].add(end);
            list[end].add(start);
        }

        visited =new int[N+1];
        visited[1] = 1;
        DFS(1);
        System.out.println(cnt);


    }
}

