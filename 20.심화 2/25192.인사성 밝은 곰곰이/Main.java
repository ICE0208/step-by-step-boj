import java.io.*;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        HashSet<String> set = new HashSet<>();
        int result = 0;

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String cur = br.readLine();
            if (cur.equals("ENTER")) {
                result += set.size();
                set.clear();
                continue;
            }

            set.add(cur);
        }

        result += set.size();
        bw.write(String.valueOf(result));
        bw.close();
        br.close();
    }
}