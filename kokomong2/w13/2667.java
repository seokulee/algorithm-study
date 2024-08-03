import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int[][] map;
    static int[][] visited;
    static PriorityQueue<Integer> homes = new PriorityQueue<>();
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int index = 0, cnt = 0;
        map = new int[n][n];
        visited = new int[n][n];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++)
                map[i][j] = line.charAt(j) - '0';
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] == 0 && map[i][j] == 1){
                    homes.add(dfs(j,i,n, 0));
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
        for (int i = 0; i < cnt; i++) {
            System.out.println(homes.poll());
        }

    }

    public static int dfs(int x, int y, int n, int cnt){
        visited[y][x] = 1;
        int max = cnt + 1;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || map[ny][nx] == 0 || visited[ny][nx] == 1)
                continue;
            max = Math.max(max , dfs(nx, ny, n, max));
        }
        return max;
    }
}