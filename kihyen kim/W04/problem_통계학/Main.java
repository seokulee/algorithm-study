import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT size, counting sorted array
		int size = Integer.parseInt(br.readLine());
		int[] arrCounting = new int[8001];
		Arrays.fill(arrCounting, 0);
		int sum = 0;
		int max = Integer.MIN_VALUE;
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < size; i++) {
			int num = Integer.parseInt(br.readLine());
			sum += num;
			max = (max < num) ? num : max;
			min = (min > num) ? num : min;

			arrCounting[4000 + num]++;
		}

		// CALC average, range(max-min)
		int avg = (int) Math.round((double) sum / size);
		int range = max - min;

		// CALC middle, mode
		int mid = -9999, cnt = 0;
		int mode = -9999, maxFreq = 0;
		boolean isDuplicated = false;
		for (int i = min+4000; i <= max+4000; i++) {
			if (arrCounting[i] < 1)
				continue;

			if (mid == -9999) {
				cnt += arrCounting[i];
				mid = (cnt > size/2) ? i-4000 : mid;
			}

			if (maxFreq < arrCounting[i]) {
				maxFreq = arrCounting[i];
				mode = i-4000;
				isDuplicated = false;
			} else if (!isDuplicated && maxFreq == arrCounting[i]) {
				mode = i-4000;
				isDuplicated = true;
			}
		}

		// PRINT
		sb	.append(avg  + "\n")
			.append(mid  + "\n")
			.append(mode + "\n")
			.append(range);
		System.out.println(sb);

	}

}