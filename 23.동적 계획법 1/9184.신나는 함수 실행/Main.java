import java.io.*;
import java.util.StringTokenizer;

public class Main {

    static int[][][] dp = new int[51][51][51];

    static int w(int a, int b, int c) {
        if (a <= 0 || b <= 0 || c <= 0) {
            return 1;
        }

        if (dp[a][b][c] != 0) {
            return dp[a][b][c];
        }

        int result = 0;
        if (a > 20 || b > 20 || c > 20) {
            result = w(20, 20, 20);
        } else if (a < b && b < c) {
            result = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c);
        } else {
            result = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1);
        }

        dp[a][b][c] = result;
        return result;
    }

    static int fib2(int n) {
        return n - 2;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        while (true) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            if (a == -1 && b == -1 && c == -1)
                break;
            bw.write(String.format("w(%d, %d, %d) = %d\n", a, b, c, w(a, b, c)));
        }
        bw.close();
        br.close();
    }
}