import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();

        int[][] dp = new int[str.length()][26];

        dp[0][str.charAt(0) - 'a'] = 1;
        for (int i = 1; i < str.length(); i++) {
            dp[i] = dp[i - 1].clone();
            dp[i][str.charAt(i) - 'a'] += 1;
        }

        int q = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            Character c = st.nextToken().charAt(0);
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            int res;
            if (start > 0) {
                res = dp[end][c - 'a'] - dp[start - 1][c - 'a'];
            } else {
                res = dp[end][c - 'a'];
            }
            bw.write(String.valueOf(res) + "\n");
        }

        bw.close();
        br.close();
    }
}