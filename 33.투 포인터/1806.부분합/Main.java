import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());

        int[] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int left = 0, right = 0;
        int curSum = arr[0];
        int result = N + 1;
        while (left <= right) {
            if (curSum >= S) {
                result = Math.min(right - left + 1, result);
                curSum -= arr[left++];
            } else {
                right += 1;
                if (right == N)
                    break;
                curSum += arr[right];
            }
        }

        System.out.println(result != N + 1 ? result : "0");
    }
}