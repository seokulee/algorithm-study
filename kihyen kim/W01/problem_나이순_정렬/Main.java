import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;
import java.util.Map.Entry;



public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        // INIT arr
        int size = Integer.parseInt(br.readLine());
        Map<Integer, List<String>> roster = new TreeMap<>();

        // INIT roster
        for(int i=0; i<size; i++) {
            String[] personInfo = br.readLine().split(" ");
            int age = Integer.parseInt(personInfo[0]);
            String name = personInfo[1];

            if(!roster.containsKey(age))
                roster.put(age, new ArrayList<String>());

            roster.get(age).add(name);
        }

        // PRINT
        for(Entry<Integer, List<String>> entryByAge : roster.entrySet()) {
            for(String name : entryByAge.getValue())
                sb.append(entryByAge.getKey()).append(' ').append(name).append('\n');
        }
        System.out.println(sb);

    }
}