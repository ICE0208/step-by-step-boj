import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        HashMap<String, Integer> map = new HashMap<>();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            if (str.length() < M)
                continue;
            map.put(str, map.getOrDefault(str, 0) + 1);
        }

        TreeSet<String> set = new TreeSet<>((o1, o2) -> {
            if (map.get(o1) != map.get(o2)) {
                return map.get(o2) - map.get(o1);
            }
            if (o1.length() != o2.length()) {
                return o2.length() - o1.length();
            }
            return o1.compareTo(o2);
        });

        for (String key : map.keySet()) {
            set.add(key);
        }
        for (String str : set) {
            bw.write(str + "\n");
        }

        br.close();
        bw.close();
    }
}