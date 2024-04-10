import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // INIT arr
        int size = 5;
        int[] arr = new int[size];
        int sum = 0;

        // INIT numbers
        for (int i = 0; i < size; i++)
            sum += (arr[i] = Integer.parseInt(br.readLine()));

        // SORT selection until mid index
        for (int i = 0; i < size / 2 + 1; i++) {
            for (int j = i; j < size; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }

        // PRINT
        int avg = sum / size;
        int mid = arr[size / 2];
        System.out.println(avg);
        System.out.println(mid);
    }
}