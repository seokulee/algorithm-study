import java.util.*;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int index = 0;
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        int[] count = new int[1000001];
        Stack<Integer> st = new Stack<>();
		StringTokenizer to = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(to.nextToken());
            count[arr[i]]++;
        }
        st.push(0);
        for (int i = 1; i < N; i++){
            index = st.peek();
            if (count[arr[index]] >= count[arr[i]])
                st.push(i);
            else if (count[arr[index]] < count[arr[i]]) {
                while (!st.isEmpty() && count[arr[st.peek()]] < count[arr[i]]){
                    arr[st.pop()] = arr[i];
                }
                st.push(i);
            }
        }
        while (!st.empty())
            arr[st.pop()] = -1;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++){
            sb.append(arr[i]).append(" ");
        }
        System.out.print(sb);
    }
}