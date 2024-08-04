import java.util.*;


class Node{
    int y;
    int x;
    int cnt;

    Node(int y, int x, int cnt){
        this.y= y;
        this.x = x;
        this.cnt = cnt;
    }

}

public class Main {

    static int[] visited;
    static int N;
    static int M;
    static int V;
    static int cnt = 0;


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        N = sc.nextInt();
        M = sc.nextInt();
        sc.nextLine();
        int[] dx = {1,0,-1,0};
        int[] dy = {0, 1,0,-1};

        int[][] arr = new int[N+1][M+1];
        int[][] visited = new int[N+1][M+1];
        for (int i = 1; i <= N; i++) {
            String a = sc.nextLine();
            for (int j = 1; j <= M; j++) {
                arr[i][j] = Character.getNumericValue(a.charAt(j-1));
            }
        }
        Queue<Node> q = new LinkedList<>();
        visited[1][1] = 1;
        q.offer(new Node(1,1,1));
        while(!q.isEmpty()){
            Node node  = q.poll();
            int x = node.x;
            int y = node.y;
            int cnt = node.cnt;

            if(y == N && x == M){
                System.out.println(cnt);
                break;
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(ny > N || nx > M|| ny <1 || nx <1){
                    continue;
                }
                if(visited[ny][nx] ==1 || arr[ny][nx] == 0){
                    continue;
                }
                visited[ny][nx] =1;
                q.offer(new Node(ny,nx,cnt+1));
            }
        }

    }
}

