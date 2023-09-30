import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    static StringBuilder sb = new StringBuilder();
    static int N, M;
    static boolean[] visited;
    static Stack<Integer> stack = new Stack<>();

    static void backtrack(int n) throws IOException {
        if (n == M) {
            stack.forEach(s -> {
                sb.append(s).append(" ");
            });
            sb.append("\n");
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (visited[i])
                continue;

            visited[i] = true;
            stack.push(i);
            backtrack(n + 1);
            visited[i] = false;
            stack.pop();
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        visited = new boolean[N + 1];

        backtrack(0);

        bw.write(sb.toString());
        bw.close();
        br.close();
    }
}