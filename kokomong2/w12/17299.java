import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static long[] num;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        String s;

        while (!(s = br.readLine()).equals("0")) {
            Stack<Integer> stack = new Stack<>();
            st = new StringTokenizer(s);
            n = Integer.parseInt(st.nextToken());
            num = new long[n];
            for (int i = 0; i < n; i++) num[i] = Long.parseLong(st.nextToken());
            long maxArea = 0;

            for (int i = 0; i < n; i++) {
                while ((!stack.isEmpty()) && num[stack.peek()] >= num[i]) {
                    long height = num[stack.pop()];
                    long weight = (stack.isEmpty()) ? i : (i - stack.peek() - 1);
                    maxArea = Math.max(maxArea, height * weight);
                }
                stack.push(i);
            }

            while (!stack.isEmpty()) {
                long height = num[stack.pop()];
                long weight = (stack.isEmpty()) ? n : (n - stack.peek() - 1);
                maxArea = Math.max(maxArea, height * weight);
            }

            sb.append(maxArea).append('\n');
        }

        System.out.println(sb);
    }

}