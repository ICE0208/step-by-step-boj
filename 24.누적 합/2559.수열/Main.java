import java.io.*;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int prev = 0;
        for (int i = 0; i < K; i++) {
            prev += arr[i];
        }
        int result = prev;

        for (int i = K; i < N; i++) {
            int cur = prev - arr[i - K] + arr[i];
            result = Math.max(result, cur);
            prev = cur;
        }

        bw.write(String.valueOf(result));
        bw.close();
        br.close();
    }
}