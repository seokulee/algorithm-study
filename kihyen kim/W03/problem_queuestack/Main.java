import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT queue, result count
		ArrayDeque<Integer> onlyQueue = new ArrayDeque<Integer>();
		int cntResult;
		{
			br.readLine(); // skip size
			String[] arrKindsOfStructure = br.readLine().split(" ");
			String[] arrStructures = br.readLine().split(" ");
			
			for(int i=0; i<arrKindsOfStructure.length; i++)
				if (arrKindsOfStructure[i].equals("0"))
					onlyQueue.addFirst( Integer.parseInt(arrStructures[i]) );

			cntResult = Integer.parseInt(br.readLine());
			for(String num : br.readLine().split(" "))
				onlyQueue.add( Integer.parseInt(num) );
		}

		// PRINT
		for(int i=0; i<cntResult; i++)
			sb.append(onlyQueue.remove()).append(" ");
		System.out.println(sb);

	}

}