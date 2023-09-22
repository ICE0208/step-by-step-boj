import java.io.*;

public class Main {
    static int fib1(int n){
        if (n==1 || n==2) return 1;
        int[] dp = new int[n+1];
        dp[1] = dp[2] = 1;
        for (int i=3; i<=n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
    static int fib2(int n) {
        return n-2;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        int result1 = fib1(N);
        int result2 = fib2(N);

        bw.write(result1 + " " + result2);
        bw.close();
        br.close();
    }
}