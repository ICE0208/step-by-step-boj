import java.io.*;
import java.util.*;

public class Main {
    static int findReplaceIndex(Stack<Integer> stack, int num) {
        int l = 0, r = stack.size() - 1;

        while (l < r) {
            int mid = l + (r - l) / 2;

            if (stack.get(mid) >= num) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }

    static int findReplaceIndex2(Stack<Integer> stack, int num) {
        int l = 0, r = stack.size() - 1;

        while (l < r) {
            int mid = l + (r - l) / 2;

            if (stack.get(mid) <= num) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int result = 0;
        Stack<Integer> stack = new Stack<>();
        ;
        for (int c = 0; c < N; c++) {

            int leftCount = 0;
            stack.clear();
            for (int i = 0; i < c; i++) {
                if (arr[i] >= arr[c])
                    continue;
                if (stack.isEmpty() || stack.peek() < arr[i]) {
                    stack.push(arr[i]);
                    leftCount++;
                    continue;
                }
                stack.set(findReplaceIndex(stack, arr[i]), arr[i]);
            }

            int rightCount = 0;
            stack.clear();
            for (int i = c + 1; i < N; i++) {
                if (arr[i] >= arr[c])
                    continue;
                if (stack.isEmpty() || stack.peek() > arr[i]) {
                    stack.push(arr[i]);
                    rightCount++;
                    continue;
                }
                stack.set(findReplaceIndex2(stack, arr[i]), arr[i]);
            }

            result = Math.max(result, leftCount + rightCount + 1);
        }

        bw.write(String.valueOf(result));
        bw.close();
        br.close();
    }
}