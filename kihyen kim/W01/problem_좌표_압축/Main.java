import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.TreeMap;
import java.util.Map.Entry;



public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // INIT arr
        int size = Integer.parseInt(br.readLine());
        int[] arr = new int[size];
        Map<Integer, Integer> coordinateCompressor = new TreeMap<>();

        // INIT coordinates & compress
        String[] coordinates = br.readLine().split(" ");
        for(int i=0; i<size; i++) {
            arr[i] = Integer.parseInt(coordinates[i]);

            if(!coordinateCompressor.containsKey(arr[i]))
                coordinateCompressor.put(arr[i], 0);
        }
        int compression = 0;
        for(Entry<Integer, Integer> entry : coordinateCompressor.entrySet()) {
            entry.setValue(compression++);
        }

        // PRINT
        for(int num : arr)
            sb.append(coordinateCompressor.get(num)).append(' ');
        System.out.println(sb);

    }

}