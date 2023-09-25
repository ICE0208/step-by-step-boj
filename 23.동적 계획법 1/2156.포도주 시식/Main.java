import java.io.*;

public class Main {
    static final int MOD = 1000000000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int[] wine = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            wine[i] = Integer.parseInt(br.readLine());
        }

        int[] dp = new int[N + 1];
        dp[1] = wine[1];
        if (N >= 2) {
            dp[2] = wine[1] + wine[2];
        }
        if (N >= 3) {
            dp[3] = Math.max(dp[2], wine[2] + wine[3]);
            dp[3] = Math.max(dp[3], dp[1] + wine[3]);
        }

        for (int i = 4; i <= N; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i]);
            dp[i] = Math.max(dp[i], dp[i - 2] + wine[i]);
        }

        bw.write(String.valueOf(dp[N]));
        bw.close();
        br.close();
    }
}