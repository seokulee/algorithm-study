import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // INIT arr
        int size = Integer.parseInt(br.readLine());
        int[] arr = new int[size];

        // INIT numbers
        for (int i = 0; i < size; i++)
            arr[i] = Integer.parseInt(br.readLine());

        // SORT (bubble)
        for (int i = 1; i < size; i++) {
            for (int j = 0; j < size - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }

        // PRINT
        for (int num : arr)
            System.out.println(num);
    }
}