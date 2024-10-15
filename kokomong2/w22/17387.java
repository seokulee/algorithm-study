
import java.io.*;
import java.util.*;

public class Main {
	static class Point {
		long x, y;

		public Point(long x, long y) {
			this.x = x;
			this.y = y;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		Point[] points = new Point[4];

		st = new StringTokenizer(br.readLine());
		long x1 = Long.parseLong(st.nextToken());
		long y1 = Long.parseLong(st.nextToken());
		long x2 = Long.parseLong(st.nextToken());
		long y2 = Long.parseLong(st.nextToken());

		st = new StringTokenizer(br.readLine());
		long x3 = Long.parseLong(st.nextToken());
		long y3 = Long.parseLong(st.nextToken());
		long x4 = Long.parseLong(st.nextToken());
		long y4 = Long.parseLong(st.nextToken());

		points[0] = new Point(x1, y1);
		points[1] = new Point(x2, y2);
		points[2] = new Point(x3, y3);
		points[3] = new Point(x4, y4);

		System.out.println(checkIntersection(points) ? 1 : 0);
		br.close();
	}

	// 두 선분이 교차하는지 여부를 확인
	public static boolean checkIntersection(Point[] points) {
		int ccw1 = ccw(points[0], points[1], points[2]);
		int ccw2 = ccw(points[0], points[1], points[3]);
		int ccw3 = ccw(points[2], points[3], points[0]);
		int ccw4 = ccw(points[2], points[3], points[1]);

		// 두 선분이 교차할 수 있는지 여부를 확인
		if (ccw1 * ccw2 <= 0 && ccw3 * ccw4 <= 0) {
			// 일직선 상에 있을 경우, 범위가 겹치는지 추가로 확인
			if (ccw1 == 0 && ccw2 == 0 && ccw3 == 0 && ccw4 == 0) {
				return areSegmentsOverlapping(points);
			}
			return true;  // 교차하는 경우
		}
		return false;  // 교차하지 않는 경우
	}

	public static int ccw(Point p1, Point p2, Point p3) {
		long crossProduct = (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x);
		if (crossProduct > 0) return 1;  // 반시계 방향
		else if (crossProduct < 0) return -1;  // 시계 방향
		else return 0;  // 일직선 상
	}

	// 일직선 상에 있을 때, 두 선분이 겹치는지 확인
	public static boolean areSegmentsOverlapping(Point[] points) {
		return Math.min(points[0].x, points[1].x) <= Math.max(points[2].x, points[3].x) &&
			Math.min(points[2].x, points[3].x) <= Math.max(points[0].x, points[1].x) &&
			Math.min(points[0].y, points[1].y) <= Math.max(points[2].y, points[3].y) &&
			Math.min(points[2].y, points[3].y) <= Math.max(points[0].y, points[1].y);
	}
}
