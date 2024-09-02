import java.util.Scanner;
import java.util.Stack;

public class Main{
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n + 1];
        int dp[] = new int[n + 1];

        for (int i = 1; i <= n; i++)
            arr[i] = sc.nextInt();

        dp[1] = 1;
        int ans = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = 1;
            for (int j = 1; j < i; j++) {
                if (arr[i] > arr[j] && dp[i] <= dp[j]) {
                    dp[i] = dp[j] + 1;
                }
            }
            ans = Math.max(ans, dp[i]);
        }

        int value = ans;
        Stack<Integer> stack = new Stack<>();

        for (int i = n; i >= 1; i--) {
            if (value == dp[i]) {
                stack.push(arr[i]);
                value--;
            }
        }

        while (!stack.isEmpty()) {
            sb.append(stack.pop() + " ");
        }

        System.out.println(ans);
        System.out.println(sb);

    }
}