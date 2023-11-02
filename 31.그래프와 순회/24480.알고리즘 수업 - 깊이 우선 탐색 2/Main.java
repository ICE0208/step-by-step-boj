import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N, M, R;
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            int u, v;
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        int[] isVisit = new int[N + 1];
        Stack<Integer> stack = new Stack<>();
        stack.add(R);

        int cnt = 1;
        while (!stack.isEmpty()) {
            int cur = stack.pop();
            if (isVisit[cur] != 0)
                continue;

            isVisit[cur] = cnt++;
            Collections.sort(graph.get(cur));
            for (int next : graph.get(cur)) {
                if (isVisit[next] != 0)
                    continue;

                stack.add(next);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(isVisit[i]).append("\n");
        }
        System.out.println(sb.toString());
        br.close();

    }
}