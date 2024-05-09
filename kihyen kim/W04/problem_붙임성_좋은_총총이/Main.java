import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, rainbowed set
		int size = Integer.parseInt(br.readLine());
		Set<String> setRainbowed = new HashSet<String>();
		setRainbowed.add("ChongChong");

		// CALC rainbowed count
		for (int i = 0; i < size; i++) {
			String[] names = br.readLine().split(" ");

			if (setRainbowed.contains(names[0]))
				setRainbowed.add(names[1]);
			if (setRainbowed.contains(names[1]))
				setRainbowed.add(names[0]);
		}

		// PRINT
		System.out.println(setRainbowed.size());

	}

}