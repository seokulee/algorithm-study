import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;
import java.util.StringTokenizer;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();

		// INIT lambda function
		Function<Object, Object> funcCalcLargestAreaOfHistogram = new Function<Object, Object>() {

			int[] arrHistogram;

			@Override
			public Object apply(Object param) {
				this.arrHistogram = (int[]) param;

				return getArea(0, arrHistogram.length - 1);
			}

			public long getArea(int lo, int hi) {
				if (lo == hi)
					return arrHistogram[lo];

				int mid = (lo + hi) / 2; // 중간지점

				long leftArea = getArea(lo, mid);
				long rightArea = getArea(mid + 1, hi);
				long centerArea = getCenterArea(lo, hi, mid);

				/*
					System.out.println("------------------------");
					System.out.println("mid: " + mid);
					System.out.println("");
					System.out.println("leftArea: " + leftArea);
					System.out.println("rightArea: " + rightArea);
					System.out.println("centerArea: " + centerArea);
					System.out.println("------------------------");
				*/

				return Math.max(Math.max(leftArea, rightArea), centerArea);
			}

			public long getCenterArea(int lo, int hi, int mid) {
				int toLeft = mid;
				int toRight = mid;

				long height = arrHistogram[mid];

				long maxArea = height;
				while (lo < toLeft && toRight < hi)
				{
					if (arrHistogram[toLeft - 1] < arrHistogram[toRight + 1]) {
						toRight += 1;
						height = Math.min(height, arrHistogram[toRight]);
					}
					else {
						toLeft -= 1;
						height = Math.min(height, arrHistogram[toLeft]);
					}

					maxArea = Math.max(maxArea, height * (toRight - toLeft + 1));
				}

				while (toRight < hi) {
					toRight++;
					height = Math.min(height, arrHistogram[toRight]);
					maxArea = Math.max(maxArea, height * (toRight - toLeft + 1));
				}
				while (lo < toLeft) {
					toLeft--;
					height = Math.min(height, arrHistogram[toLeft]);
					maxArea = Math.max(maxArea, height * (toRight - toLeft + 1));
				}

				return maxArea;
			}

		};

		// RUN
		while (true)
		{
			// INIT size
			StringTokenizer st = new StringTokenizer(br.readLine());
			int size = Integer.parseInt(st.nextToken()); // skip size
			if (size == 0)
				break;

			// INIT array of histogram
			int[] arrHistogram = new int[size];
			for (int i = 0; i < size; i++)
				arrHistogram[i] = Integer.parseInt(st.nextToken());

			// CALC
			sb
				.append((long) funcCalcLargestAreaOfHistogram.apply(arrHistogram))
				.append('\n');
		}

		// PRINT
		System.out.println(sb);

	}

}