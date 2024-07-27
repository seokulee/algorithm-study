import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int index = 0;
        int N = sc.nextInt();
        int[] arr = new int[N];
        Stack<Integer> st = new Stack<>();
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        st.push(0);
        for (int i = 1; i < N; i++){
            index = st.peek();
            if (arr[index] > arr[i])
                st.push(i);
            else if (arr[index] <= arr[i]) {
                while (!st.isEmpty() && arr[st.peek()] < arr[i]){
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