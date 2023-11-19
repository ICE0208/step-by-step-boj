import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] coins = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        int[] dp = new int[k + 1];
        dp[0] = 1;

        for (int coinI = 1; coinI <= n; coinI++) {
            for (int target = 1; target <= k; target++) {
                int a = dp[target];
                int b = target - coins[coinI] >= 0 ? dp[target - coins[coinI]] : 0;
                dp[target] = a + b;
            }
        }

        System.out.println(dp[k]);
        br.close();
    }
}