import java.io.*;
import java.util.StringTokenizer;

public class Main {

    static int N;
    static boolean[] visited;
    static int[][] arr;
    static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        visited = new boolean[N];
        arr = new int[N][N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dfs(0, -1);
        bw.write(String.valueOf(result));

        bw.close();
        br.close();

    }

    static void dfs(int n, int lastIndex) {
        if (n == Math.floor(N / 2)) {
            result = Math.min(result, calc());
            return;
        }

        for (int i = lastIndex + 1; i < N; i++) {
            if (visited[i] == true)
                continue;

            visited[i] = true;
            dfs(n + 1, i);
            visited[i] = false;
        }
    }

    static int calc() {
        int aSum = 0;
        int bSum = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (visited[i] == visited[j]) {
                    if (visited[i] == true) {
                        aSum += (arr[i][j] + arr[j][i]);
                    } else {
                        bSum += (arr[i][j] + arr[j][i]);
                    }
                }
            }
        }
        return Math.abs(aSum - bSum);
    }
}