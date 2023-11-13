import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int n = Integer.parseInt(br.readLine());
            int[] arr = new int[n];

            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < arr.length; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            List<Set<Integer>> next = new ArrayList<>();
            for (int i = 0; i <= arr.length; i++) {
                next.add(new HashSet<>());
            }
            int[] inDegree = new int[n + 1];

            Set<Integer> tempSet = new HashSet<>();
            int tempCnt = n - 1;
            for (int i = n - 1; i >= 0; i--) {
                inDegree[arr[i]] = tempCnt--;
                next.get(arr[i]).addAll(tempSet);
                tempSet.add(arr[i]);
            }

            int m = Integer.parseInt((br.readLine()));
            while (m-- > 0) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                if (next.get(b).contains(a)) {
                    // b->a -> a->b
                    next.get(b).remove(a);
                    inDegree[a] -= 1;
                    next.get(a).add(b);
                    inDegree[b] += 1;
                } else {
                    // a->b -> b->a
                    next.get(a).remove(b);
                    inDegree[b] -= 1;
                    next.get(b).add(a);
                    inDegree[a] += 1;
                }
            }

            Stack<Integer> stack = new Stack<>();
            for (int i = 1; i <= n; i++) {
                if (inDegree[i] == 0) {
                    stack.add(i);
                }
            }

            StringBuilder tempSb = new StringBuilder();
            int cnt = 0;
            while (!stack.isEmpty()) {
                if (stack.size() > 1) {
                    break;
                }

                int cur = stack.pop();
                cnt += 1;
                tempSb.append(cur).append(" ");

                for (int ne : next.get(cur)) {
                    inDegree[ne] -= 1;
                    if (inDegree[ne] == 0) {
                        stack.add(ne);
                    }
                }
            }

            if (cnt == n) {
                sb.append(tempSb).append("\n");
            } else {
                sb.append("IMPOSSIBLE").append("\n");
            }
        }

        System.out.println(sb.toString());
    }
}