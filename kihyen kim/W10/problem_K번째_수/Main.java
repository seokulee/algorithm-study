import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Supplier;



public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, target num
		int size = Integer.parseInt(br.readLine());
		int target = Integer.parseInt(br.readLine());

		// INIT lambda function
		Supplier<Object> funcBinarySearch = new Supplier<Object>() {

			int result;

			@Override
			public Object get() {
				binarySearch(1, target);

				return result;
			}

			int binarySearch(int left, int right) {
				if (left > right)
					return right;

				int mid = (left + right) / 2;

				int cnt = 0;
				for (int i = 1; i <= size; i++)
					cnt += Math.min(mid / i, size);

				if (cnt < target)
					return binarySearch(mid + 1, right);
				else {
					result = mid;
					return binarySearch(left, mid - 1);
				}
			}

		};

		// PRINT
		System.out.println((int) funcBinarySearch.get());

	}

}