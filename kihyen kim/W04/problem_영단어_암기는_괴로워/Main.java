import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Map;
import java.util.HashMap;
import java.util.TreeMap;
import java.util.TreeSet;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, length for ignore, words
		StringTokenizer st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());
		int lenIgnore = Integer.parseInt(st.nextToken());
		Map<String, Integer> mapWords = new HashMap<String, Integer>();
		for (int i = 0; i < size; i++)
		{
			String word = br.readLine();
			if (word.length() < lenIgnore)
				continue;

			mapWords.merge(word, 1, Integer::sum);
			// ↑ this means same ↓
			//	if (mapWords.containsKey(word))
			//		mapWords.put(word, 1);
			//	else
			//		mapWords.put(word, mapWords.get(word)+1);
		}
		
		// SORT
		TreeMap<Integer, TreeMap<Integer, TreeSet<String>>> sortedWords = new TreeMap<Integer, TreeMap<Integer, TreeSet<String>>>();
		for (String word : mapWords.keySet())
		{
			int len = word.length();
			int freq = mapWords.get(word);

			if (!sortedWords.containsKey(freq)) {
				sortedWords.put(freq, new TreeMap<Integer, TreeSet<String>>());
				for (int i = lenIgnore; i <= 10; i++)
					sortedWords.get(freq).put(i, new TreeSet<String>());
			}
			sortedWords.get(freq).get(len).add(word);
		}
		
		// PRINT
		for (int keyFreq : sortedWords.descendingKeySet()) {
			for (int keyLen : sortedWords.get(keyFreq).descendingKeySet())
				for (String word : sortedWords.get(keyFreq).get(keyLen))
					sb.append(word).append("\n");
		}
		System.out.println(sb);

	}

}