import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.function.Function;

public class Main {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		// INIT size, matrix of image
		int size = Integer.parseInt(br.readLine());
		boolean[][] matrix = new boolean[size][size];
		for (int i = 0; i < size; i++) {
			String str = br.readLine();
			for (int j = 0; j < size; j++)
				matrix[i][j] = str.charAt(j) == '1';
		}
		
		// INIT lamda function
		Function<Object, Object> funcGenerateQuadTree = new Function<Object, Object>() {
			
			boolean[][] matrix;
			StringBuilder result;

			@Override
			public Object apply(Object param) {
				this.matrix = (boolean[][])param;
				this.result = new StringBuilder();
				
				recursion(0, 0, matrix.length);
				
				return result;
			}

			public void recursion(int idxY, int idxX, int size) {
				boolean isMono = true;
				for (int y = idxY; y<idxY+size; y++) {
					for (int x = idxX; x<idxX+size; x++)
						if(matrix[y][x] != matrix[idxY][idxX]) {
							isMono = false;
							break;
						}
				}
				
				if (isMono) {
					result.append(matrix[idxY][idxX] ? "1" : "0");
					return;
				}

				result.append("(");
				recursion(idxY, idxX, size/2);
				recursion(idxY, idxX + size/2, size/2);
				recursion(idxY + size/2, idxX, size/2);
				recursion(idxY + size/2, idxX + size/2, size/2);
				result.append(")");
			}
		};

		// CALC & PRINT
		System.out.println( (StringBuilder)funcGenerateQuadTree.apply(matrix) );

	}

}