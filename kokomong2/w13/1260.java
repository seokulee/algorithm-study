import java.util.*;


public class Main {

    static int[] visited = new int[1001];
    static int N;
    static int M;
    static int V;
    static ArrayList<Integer>[] list;
    static StringBuilder sb = new StringBuilder();
    static StringBuilder sb2 = new StringBuilder();


    static void DFS(int start){
        for (int end : list[start]) {
            int next = end;
            if(visited[next] ==0 ){
                visited[next]=1;
                sb.append(" " +next);
                DFS(next);
            }
        }

    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        V = sc.nextInt();
        list = new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            list[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            list[start].add(end);
            list[end].add(start); // 양방향 때문에 추가해줌
        }
        for (int i = 1; i <= N; i++) {
            Collections.sort(list[i]);
        }

        sb.append(V);
        visited[V] = 1;
        DFS(V);
        System.out.println(sb);

        visited = new int[1001];
        Queue<Integer> q = new LinkedList<>();
        visited[V] = 1;
        q.offer(V);
        while (!q.isEmpty()){
            int start = q.poll();
            sb2.append(" " + start);

            for(int end :list[start]){
                if(visited[end]==0){
                    visited[end] = 1;
                    q.offer(end);
                }
            }
        }
        System.out.println(sb2.deleteCharAt(0));
    }
}
