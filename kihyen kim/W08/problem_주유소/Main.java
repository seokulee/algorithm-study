import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, array of meters, array of distances, array of fuel costs
		int size = Integer.parseInt(br.readLine());
		int[] arrDistances = new int[size - 1];
		int[] arrFuelCosts = new int[size];
		{			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < arrDistances.length; i++)
				arrDistances[i] = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < arrFuelCosts.length; i++)
				arrFuelCosts[i] = Integer.parseInt(st.nextToken());
		}

		// CALC
		long result = 0;
		int minFuelCost = arrFuelCosts[0];
		for (int i = 0; i < arrDistances.length; i++)
		{
			result += (long) minFuelCost * arrDistances[i];

			minFuelCost = Math.min(minFuelCost, arrFuelCosts[i + 1]);
		}
		
		// PRINT
		System.out.println(result);

	}

}