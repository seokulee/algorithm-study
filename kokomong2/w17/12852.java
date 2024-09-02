
import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();

		int[] dp = new int[N + 1];
		int[] before = new int[N + 1];

		StringBuilder str = new StringBuilder();

		dp[1] = 0;

		for(int i = 2; i <= N; i++) {
			dp[i] = dp[i - 1] + 1;
			before[i] = i - 1;

			if (i % 3 == 0 && dp[i / 3] + 1 < dp[i]) {
				dp[i] = dp[i / 3] + 1;
				before[i] = i / 3;
			}
			if (i % 2 == 0 && dp[i / 2] + 1 < dp[i]) {
				dp[i] = dp[i / 2] + 1;
				before[i] = i / 2;
			}
		}
		System.out.println(dp[N]);

		while(N > 0){
			str.append(N).append(" ");
			N = before[N];
		}

		System.out.print(str);
	}
}
