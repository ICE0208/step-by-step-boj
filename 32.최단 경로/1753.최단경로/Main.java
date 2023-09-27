import java.io.*;
import java.util.*;

public class Main {
    static int INF = 20000 * 10;

    public static <T> void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(br.readLine());

        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= V; i++)
            graph.add(new ArrayList<>());

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            graph.get(u).add(new int[] { v, w });
        }

        int[] distance = new int[V + 1];
        for (int i = 0; i <= V; i++) {
            distance[i] = INF;
        }
        distance[start] = 0;

        Queue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });

        q.offer(new int[] { start, 0 });

        while (q.isEmpty() == false) {
            int[] cur = q.poll();
            int curNode = cur[0];
            int curDist = cur[1];

            if (curDist > distance[curNode])
                continue;

            for (int[] next : graph.get(curNode)) {
                int nextNode = next[0];
                int needDist = next[1];
                int nextDist = curDist + needDist;

                if (nextDist < distance[nextNode]) {
                    distance[nextNode] = nextDist;
                    q.offer(new int[] { nextNode, nextDist });
                }
            }
        }

        for (int i = 1; i <= V; i++) {
            if (distance[i] == INF) {
                bw.write("INF\n");
                continue;
            }
            bw.write(String.valueOf(distance[i]) + "\n");
        }

        br.close();
        bw.close();
    }

}
