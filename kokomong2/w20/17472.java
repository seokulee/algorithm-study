import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] map;
    static boolean[][] visited;
    static int[] dx = {0, 1, 0, -1}; // 상하좌우 탐색을 위한 방향 배열
    static int[] dy = {1, 0, -1, 0};
    static List<Edge> edges;
    static int[] parent;

    static class Edge implements Comparable<Edge> {
        int from, to, weight;

        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return Integer.compare(this.weight, other.weight);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[N][M];
        visited = new boolean[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int islandId = 2;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 1 && !visited[i][j]) {
                    markIsland(i, j, islandId++);
                }
            }
        }

        edges = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] > 1) {
                    buildBridge(i, j, map[i][j]);
                }
            }
        }

        Collections.sort(edges);
        parent = new int[islandId];
        for (int i = 2; i < islandId; i++) {
            parent[i] = i;
        }

        int totalWeight = 0;
        int edgesUsed = 0;

        for (Edge edge : edges) {
            if (union(edge.from, edge.to)) {
                totalWeight += edge.weight;
                edgesUsed++;
                if (edgesUsed == islandId - 3) {
                    break;
                }
            }
        }

        if (edgesUsed != islandId - 3) {
            System.out.println(-1);
        } else {
            System.out.println(totalWeight);
        }
    }

    static void markIsland(int x, int y, int islandId) {
        visited[x][y] = true;
        map[x][y] = islandId;

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx >= 0 && ny >= 0 && nx < N && ny < M && !visited[nx][ny] && map[nx][ny] == 1) {
                markIsland(nx, ny, islandId);
            }
        }
    }

    static void buildBridge(int x, int y, int islandId) {
        for (int d = 0; d < 4; d++) {
            int nx = x;
            int ny = y;
            int length = 0;

            while (true) {
                nx += dx[d];
                ny += dy[d];

                if (nx < 0 || ny < 0 || nx >= N || ny >= M || map[nx][ny] == islandId) {
                    break;
                }

                if (map[nx][ny] == 0) {
                    length++;
                } else if (map[nx][ny] > 1 && length >= 2) {
                    edges.add(new Edge(islandId, map[nx][ny], length));
                    break;
                } else {
                    break;
                }
            }
        }
    }

    static int find(int x) {
        if (x == parent[x]) return x;
        return parent[x] = find(parent[x]);
    }

    static boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            parent[rootY] = rootX;
            return true;
        }
        return false;
    }
}
