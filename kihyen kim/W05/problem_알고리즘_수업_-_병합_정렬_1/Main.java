import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	
	static int 	cntTestPoint = 0,
				cntSaved = 0,
				numSavedAtTestPoint = -1;
	
	public static void mergeSort(int[] A, int idxStart, int idxEnd) {
		if (idxStart < idxEnd) {
			int idxMiddle = (idxStart + idxEnd) / 2;
			mergeSort(A, idxStart, idxMiddle);
			mergeSort(A, idxMiddle+1, idxEnd);
			merge(A, idxStart, idxMiddle, idxEnd);
		}
	}
	public static void merge(int[] A, int idxStart, int idxMiddle, int idxEnd) {

		if (numSavedAtTestPoint != -1)
			return;
		
		int idxLeft  = idxStart,
			idxRight = idxMiddle+1,
			t = 0;
		int[] tmp = new int[idxEnd - idxStart + 1]; // 임시 배열 생성

		// 두 개의 배열을 비교하면서 작은 값을 임시 배열에 저장
		while (idxLeft <= idxMiddle && idxRight <= idxEnd) {
			if (A[idxLeft] <= A[idxRight]) {
				tmp[t++] = A[idxLeft++]; // 왼쪽 배열의 값을 임시 배열에 저장하고 인덱스 증가
			} else {
				tmp[t++] = A[idxRight++]; // 오른쪽 배열의 값을 임시 배열에 저장하고 인덱스 증가
			}
		}

		// 왼쪽 배열이 남은 경우
		while (idxLeft <= idxMiddle)
			tmp[t++] = A[idxLeft++];

		// 오른쪽 배열이 남은 경우
		while (idxRight <= idxEnd)
			tmp[t++] = A[idxRight++];

		// 임시 배열의 값을 원래 배열에 복사
		for (int i = 0; i < tmp.length; i++) {
			
			if(++cntSaved == cntTestPoint)
				numSavedAtTestPoint = tmp[i];

			A[idxStart + i] = tmp[i];
		}
	}

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		// INIT size, numbers
		st = new StringTokenizer(br.readLine());
		int size = Integer.parseInt(st.nextToken());

		// INIT numbers
		cntTestPoint = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		int[] arr = new int[size];
		for (int i = 0; i < size; i++)
			arr[i] = Integer.parseInt(st.nextToken());
		
		// SORT until (++cntSaved == cntTestPoint)
		mergeSort(arr, 0, arr.length - 1);
		
		// PRINT
		System.out.println(numSavedAtTestPoint);

	}

}