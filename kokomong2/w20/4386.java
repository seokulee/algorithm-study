import org.w3c.dom.Node;

import java.io.*;
import java.util.*;

public class Main {


    static class Union {

        int[] parent, rank;

        public Union (int N) {
            parent = new int[N];
            rank = new int[N];

            for (int i = 0; i < N; i++) {
                parent[i] = i;
            }
        }

        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }

        boolean union (int x, int y) {
            int rootX  = find(x);
            int rootY  = find(y);

            if (rootX != rootY) {
                if (rank[x] > rank[y]) {
                    parent[rootY] = rootX;
                } else if(rank[x] < rank[y]) {
                    parent[rootX] = rootY;
                } else {
                    parent[rootY] = rootX;
                    rank[rootX]++;
                }
                return true;
            } else {
                return false;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        double[][] stars = new double[N][2];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            stars[i][0] = Double.parseDouble(st.nextToken());
            stars[i][1] = Double.parseDouble(st.nextToken());
        }

        List<Edge> edges = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                double weight = Math.sqrt(Math.pow(stars[i][0] - stars[j][0], 2) + Math.pow(stars[i][1] - stars[j][1], 2));
                edges.add(new Edge(i, j, weight));
            }
        }
        Collections.sort(edges);
        Union union = new Union(N);

        double sum = 0;
        for (Edge edge : edges) {
            if (union.union(edge.start, edge.end))
                sum += edge.weight;
        }

        bw.write(String.format("%.2f", sum));
        bw.flush();
        bw.close();
        br.close();
    }
}

class Edge implements Comparable<Edge>{

    int start;
    int end;
    double weight;

    public Edge(int start, int end, double weight) {
        this.start = start;
        this.end = end;
        this.weight = weight;
    }

    @Override
    public int compareTo (Edge o) {
        return Double.compare(this.weight, o.weight);
    }
}