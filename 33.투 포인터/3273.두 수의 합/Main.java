import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        // 입력
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int x = Integer.parseInt(br.readLine());

        // 투 포인터 연산 준비
        Arrays.sort(arr);
        int left = 0, right = n - 1;
        int cnt = 0;

        // 투 포인터 연산 시작
        while (left < right) {
            int cur = arr[left] + arr[right];

            if (cur == x) {
                cnt++;
                left++;
                right--;
            } else if (cur > x) {
                right--;
            } else
                left++;
        }

        // 출력
        bw.write(String.valueOf(cnt));
        bw.close();
        br.close();
    }
}