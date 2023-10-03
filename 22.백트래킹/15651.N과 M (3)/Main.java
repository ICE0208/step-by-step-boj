import java.io.*;
import java.util.*;

public class Main {

    static int[] arr = new int[7];
    static int N, M;
    static StringBuilder sb = new StringBuilder();

    static void backtrack(int n) {
        if (n == M) {
            for (int i = 0; i < M; i++) {
                sb.append(arr[i]).append((" "));
            }
            sb.append("\n");
            return;
        }

        for (int i = 1; i < N + 1; i++) {
            arr[n] = i;
            backtrack(n + 1);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        backtrack(0);
        bw.write(sb.toString());
        bw.close();
        br.close();
    }
}