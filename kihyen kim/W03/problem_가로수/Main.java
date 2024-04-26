import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

	static int getGcd(int a, int b) {
		int euclidean = (a > b) ? a : b;
		int divisor = (a > b) ? b : a;

		while (divisor != 0) {
			int temp = divisor;
			divisor = euclidean % divisor;
			euclidean = temp;
		}

		return euclidean;
	}

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, positions
		int size = Integer.parseInt(br.readLine());
		int[] arrPosition = new int[size];
		for (int i = 0; i < size; i++)
			arrPosition[i] = Integer.parseInt(br.readLine());

		// CALC targetDistance
		int targetDistance = 0;
		for (int i = 0; i < size - 1; i++) {
			int distance = arrPosition[i + 1] - arrPosition[i];
			targetDistance = getGcd(distance, targetDistance);
		}

		// CALC count blanked
		int cntBlanked = 0;
		{
			int index = 0;
			int nextPosition;
			while (true) {
				if (index + 1 == size)
					break;

				nextPosition = arrPosition[index] + targetDistance;
				if (arrPosition[index + 1] == nextPosition)
					index++;
				else {
					cntBlanked++;
					arrPosition[index] = nextPosition;
				}
			}
		}

		// PRINT
		sb.append(cntBlanked);
		System.out.println(sb);

	}

}