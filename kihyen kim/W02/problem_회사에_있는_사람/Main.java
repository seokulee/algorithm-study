import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Map;
import java.util.TreeMap;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // INIT workers
        TreeMap<String, Boolean> mapWorkers = new TreeMap<String, Boolean>();
        {
            int size = Integer.parseInt(br.readLine());
            for (int i = 0; i < size; i++) {
                String log = br.readLine();
                String name = log.split(" ")[0];

                if (log.contains("enter"))
                    mapWorkers.put(name, true);
                else
                    mapWorkers.remove(name);
            }
        }

        // PRINT
        for (Map.Entry<String, Boolean> entry : mapWorkers.descendingMap().entrySet())
            sb.append(entry.getKey()).append("\n");

        System.out.println(sb);

    }

}