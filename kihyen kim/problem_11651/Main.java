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
        Map<Integer, Map<Integer, Boolean>> coordinate = new TreeMap<>();

        // INIT coordinates
        for(int i=0; i<size; i++) {
            String[] strXY = br.readLine().split(" ");
            int xpos = Integer.parseInt(strXY[0]);
            int ypos = Integer.parseInt(strXY[1]);

            if(!coordinate.containsKey(ypos))
                coordinate.put(ypos, new TreeMap<Integer, Boolean>());

            coordinate.get(ypos).put(xpos, true);
        }

        // PRINT
        for(Entry<Integer, Map<Integer, Boolean>> entryYpos : coordinate.entrySet()) {
            for(Entry<Integer, Boolean> entryXpos : entryYpos.getValue().entrySet())
                sb.append(entryXpos.getKey()).append(' ').append(entryYpos.getKey()).append('\n');
        }
        System.out.println(sb);

    }
}