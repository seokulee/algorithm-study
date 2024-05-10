import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;

public class Main {

	//	public static String recursion(String s, int l, int r) {
	//		if (l >= r)
	//			return ("1 " + ++l);
	//		else
	//		if (s.charAt(l) != s.charAt(r))
	//			return ("0 " + ++l);
	//		else
	//			return recursion(s, l + 1, r - 1);
	//	}
	//	public static String isPalindrome(String s) {
	//		return recursion(s, 0, s.length() - 1);
	//	}

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size
		int size = Integer.parseInt(br.readLine());
		
		// INIT palindrome lamda function
		Function<String, String> funcIsPalindrome = new Function<String, String>() {
			@Override
			public String apply(String s) {
				return apply(s, 0, s.length() - 1);
			}
			public String apply(String s, int l, int r) {
				if (l >= r)
					return ("1 " + ++l);
				else
				if (s.charAt(l) != s.charAt(r))
					return ("0 " + ++l);
				else
					return apply(s, l + 1, r - 1);
			}
		};

		// PRINT
		//	for (int i = 0; i < size; i++)
		//		System.out.println(isPalindrome(br.readLine()));
		for (int i = 0; i < size; i++)
			System.out.println(funcIsPalindrome.apply(br.readLine()));

	}

}