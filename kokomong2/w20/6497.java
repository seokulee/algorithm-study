import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Edge implements Comparable<Edge> {
    int u, v, weight;

    public Edge(int u, int v, int weight) {
        this.u = u;
        this.v = v;
        this.weight = weight;
    }

    @Override
    public int compareTo(Edge o) {
        return this.weight - o.weight;
    }
}

class UnionFind {
    private int[] parent, rank;

    public UnionFind(int n) {
        parent = new int[n];
        rank = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            rank[i] = 1;
        }
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX == rootY) {
            return false;
        }

        if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
        return true;
    }
}

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while (true) {
            String[] line = br.readLine().split(" ");
            int m = Integer.parseInt(line[0]);
            int n = Integer.parseInt(line[1]);

            if (m == 0 && n == 0) {
                break;
            }

            List<Edge> edges = new ArrayList<>();
            int totalCost = 0;

            for (int i = 0; i < n; i++) {
                line = br.readLine().split(" ");
                int u = Integer.parseInt(line[0]);
                int v = Integer.parseInt(line[1]);
                int weight = Integer.parseInt(line[2]);
                edges.add(new Edge(u, v, weight));
                totalCost += weight;
            }

            Collections.sort(edges);
            UnionFind uf = new UnionFind(m);

            int mstCost = 0;
            int edgeCount = 0;

            for (Edge edge : edges) {
                if (uf.union(edge.u, edge.v)) {
                    mstCost += edge.weight;
                    edgeCount++;
                    if (edgeCount == m - 1) {
                        break;
                    }
                }
            }

            int savedCost = totalCost - mstCost;
            bw.write(savedCost + "\n");
        }

        bw.flush();
        br.close();
        bw.close();
    }
}
