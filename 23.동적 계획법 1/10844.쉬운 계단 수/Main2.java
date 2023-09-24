import java.io.*;

// 제출할 때는 Main2를 Main으로 바꿔줘야 함
public class Main2 {
    static final int DIVIDE = 1000000000;
    static final int[][] dp = new int[101][10]; // (1~100), (0~9)
    static int N;

    static int k(int depth, int curNum) {
        if (depth == N)
            return 1;
        if (dp[depth][curNum] != 0)
            return dp[depth][curNum];

        if (1 <= curNum && curNum <= 8) {
            dp[depth][curNum] = (k(depth + 1, curNum - 1) + k(depth + 1, curNum + 1)) % DIVIDE;
        } else if (curNum == 0) {
            dp[depth][curNum] = k(depth + 1, 1) % DIVIDE;
        } else { // curNum == 9
            dp[depth][curNum] = k(depth + 1, 8) % DIVIDE;
        }

        return dp[depth][curNum];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());

        int sum = 0;
        for (int i = 1; i <= 9; i++) {
            sum = (sum + k(1, i)) % DIVIDE;
        }

        bw.write(String.valueOf(sum));
        bw.close();
        br.close();
    }
}