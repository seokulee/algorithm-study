import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, k;
    static int[] arr;
    static Queue<Integer> q = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());


        if (n >= k) {
            System.out.println(n - k);
        } else {
            System.out.println(bfs());
        }

    }

    static int bfs() {

        arr = new int[100001];
        q.add(n);
        arr[n] = 1;
        while (!q.isEmpty()) {
            int x = q.poll();
            for (int i = 0; i < 3; i++) {
                int nx;
                if (i == 0)
                    nx = x - 1;
                else if (i == 1)
                    nx = x + 1;
                else
                    nx = x * 2;

                if (nx == k)
                    return arr[x];

                if (nx >= 0 && nx < 100001 && arr[nx] == 0) {
                    arr[nx] = arr[x] + 1;
                    q.add(nx);
                }
            }
        }
        return 0;
    }
}
