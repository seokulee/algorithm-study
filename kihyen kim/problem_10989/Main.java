import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // INIT arr
        int size = Integer.parseInt(br.readLine());
        int[] arr = new int[10000];

        // INIT numbers by counting using int array within the given range
        for (int i = 0; i < size; i++) {
            int num = Integer.parseInt(br.readLine());
            arr[num - 1]++;
        }

        // PRINT
        for (int num = 1; num <= arr.length; num++) {
            for (int i = 0; i < arr[num - 1]; i++)
                sb.append(num).append('\n');
        }
        System.out.println(sb);
    }
}