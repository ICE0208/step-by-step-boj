import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        int left = 0, right = N - 1;
        int[] result = new int[] { Integer.MAX_VALUE }; // 특성값, 용액1, 용액2
        while (left < right) {
            int cur = arr[left] + arr[right];
            if (Math.abs(cur) < Math.abs(result[0])) {
                result = new int[] { cur, arr[left], arr[right] };
            }

            if (cur > 0) {
                right--;
            } else {
                left++;
            }
        }

        bw.write(result[1] + " " + result[2]);
        bw.close();
        br.close();
    }
}