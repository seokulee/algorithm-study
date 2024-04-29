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
        Map<Integer, Map<String, Boolean>> dictionary = new TreeMap<>();

        // INIT words
        for(int i=0; i<size; i++) {
            String word = br.readLine();

            if(!dictionary.containsKey(word.length()))
                dictionary.put(word.length(), new TreeMap<String, Boolean>());

            dictionary.get(word.length()).put(word, true);
        }

        // PRINT
        for(Entry<Integer, Map<String, Boolean>> entryByWordLength : dictionary.entrySet()) {
            for(Entry<String, Boolean> entryByWordStr : entryByWordLength.getValue().entrySet())
                sb.append(entryByWordStr.getKey()).append('\n');
        }
        System.out.println(sb);

    }
}