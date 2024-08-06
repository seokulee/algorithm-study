import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int[] dx = {1,2,2,1,-1,-2,-2,-1};
    static int[] dy = {2,1,-1,-2,-2,-1,1,2};

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x, y, l, nx, ny, cnt , resx, resy;
        for (int i = 0; i < n; i++) {
            l = sc.nextInt();
            Queue<Pair> q = new LinkedList<>();
            int[][] visited = new int[l][l];
            x = sc.nextInt();
            y = sc.nextInt();
            resx = sc.nextInt();
            resy = sc.nextInt();
            cnt = 0;
            visited[y][x] = 1;
            q.add(new Pair(x,y, cnt,visited));
            while (!q.isEmpty()){
                Pair pair = q.poll();
                x = pair.x;
                y = pair.y;
                if (x == resx && y == resy) {
                    System.out.println(pair.cnt);
                    break;
                }
                for (int j = 0; j < 8; j++) {
                    nx = x + dx[j];
                    ny = y + dy[j];
                    if (nx < l && ny < l && nx >= 0 && ny >= 0 && pair.visited[ny][nx] == 0) {
                        pair.visited[ny][nx] = 1;
                        q.add(new Pair(nx, ny, pair.cnt + 1, pair.visited));
                    }
                }
            }
        }
    }
}

class Pair{
    int x;
    int y;
    int cnt;
    int[][] visited;
    public Pair(int x, int y, int cnt, int[][] visited) {
        this.x = x;
        this.y = y;
        this.cnt = cnt;
        this.visited = visited;
    }
}