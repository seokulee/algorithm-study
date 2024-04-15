import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;



public class Main {
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] inputs1 = br.readLine().split(" ");
		String[] inputs2 = br.readLine().split(" ");
		
		// INIT arr
		int size = Integer.parseInt(inputs1[0]);
		int indexCutline = Integer.parseInt(inputs1[1]) - 1;
		int[] arr = new int[size];
		
		// INIT numbers
		for(int i=0; i<size; i++)
			arr[i] = Integer.parseInt(inputs2[i]);

		// SORT selection until cutline index
		for(int i=0; i<indexCutline+1; i++) {
			for(int j=i; j<size; j++) {
				if(arr[i]<arr[j]) {
					int temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
		}
		
		// PRINT
		System.out.println(arr[indexCutline]);
	}
}