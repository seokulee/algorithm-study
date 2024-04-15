import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // INIT arr
        int size = Integer.parseInt(br.readLine());
        boolean[] arr = new boolean[2000001];

        // INIT numbers using boolean array within the given range
        for (int i = 0; i < size; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[num + 1000000] = true;
        }

        // PRINT
        for (int i = 0; i < arr.length; i++) {
            if (arr[i]) {
                sb.append(i - 1000000);
                sb.append('\n');
            }
        }
        System.out.print(sb);
    }
}
