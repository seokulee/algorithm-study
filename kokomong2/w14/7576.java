import java.util.*;

public class Main {

    static class Pair{
        int x,y;
        Pair(int y, int x){
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int M  =sc.nextInt();
        int N  = sc.nextInt();
        int[][] arr = new int[N][M];
        int[][] visited = new int[N][M];
        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};

        ArrayList<Pair> pairlist = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = sc.nextInt();
                if(arr[i][j] ==1){
                    pairlist.add(new Pair(i,j));
                }
            }
        }
        Queue<Pair> q = new LinkedList<>();
        for (Pair pair :pairlist) {
            q.offer(pair);
        }
        int cnt=0;
        int hmt = q.size();
        int H = 0;


        while(!q.isEmpty()){
            Pair pair = q.poll();
            H++;
            int x = pair.x;
            int y = pair.y;
            for (int i = 0; i < 4; i++) {
                int nx = x+dx[i];
                int ny = y+dy[i];

                if(ny>=N|| nx >=M || nx<0|| ny<0){
                    continue;
                }
                if(arr[ny][nx]==1|| visited[ny][nx] ==1||arr[ny][nx]==-1){
                    continue;
                }
                visited[ny][nx] =1;
                arr[ny][nx] =1;
                q.offer(new Pair(ny,nx));
            }
            if(hmt == H){
                cnt ++;
                hmt = q.size();

                H =0;
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if(arr[i][j] ==0){
                    System.out.println(-1);
                    System.exit(0);
                }
            }
        }

        System.out.println((cnt-1));


    }
}

