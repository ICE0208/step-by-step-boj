import java.io.*;
import java.util.Arrays;

public class Main {

    static int N;
    static int[] nums;
    static int[] opersCnt;
    static int max = (int) Math.pow(-10, 9);
    static int min = (int) Math.pow(10, 9);

    static void bt(int n, int result) {
        if (N == n) {
            max = Math.max(max, result);
            min = Math.min(min, result);
            return;
        }

        if (opersCnt[0] > 0) {
            opersCnt[0] -= 1;
            bt(n + 1, result + nums[n]);
            opersCnt[0] += 1;
        }
        if (opersCnt[1] > 0) {
            opersCnt[1] -= 1;
            bt(n + 1, result - nums[n]);
            opersCnt[1] += 1;
        }
        if (opersCnt[2] > 0) {
            opersCnt[2] -= 1;
            bt(n + 1, result * nums[n]);
            opersCnt[2] += 1;
        }
        if (opersCnt[3] > 0) {
            opersCnt[3] -= 1;
            bt(n + 1, (int) result / nums[n]);
            opersCnt[3] += 1;
        }
    }

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        N = Integer.parseInt(br.readLine());
        nums = Arrays.stream(br.readLine().split((" "))).mapToInt(Integer::parseInt).toArray();
        opersCnt = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        bt(1, nums[0]);

        bw.write(String.valueOf(max));
        bw.write("\n");
        bw.write(String.valueOf(min));

        br.close();
        bw.close();
    }
}
