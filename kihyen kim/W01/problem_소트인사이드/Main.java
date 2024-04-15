import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;



public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // INIT string
        String str = br.readLine();

        // INIT arr
        int[] arr = new int[10];
        for(char c : str.toCharArray())
            arr[Character.getNumericValue(c)]++;

        // PRINT
        for(int num=9; num>=0; num--) {
            for(int i=0; i<arr[num]; i++)
                sb.append(num);
        }
        System.out.print(sb);

    }

}