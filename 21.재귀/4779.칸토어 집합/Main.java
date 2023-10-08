import java.io.*;

public class Main {
    static int last = 0;
    static StringBuilder sb = new StringBuilder();

    static void removeCenter(int start, int end) {
        int len = end - start + 1;
        if (len == 1) {
            // 전꺼 출력
            for (int i = last + 1; i < end; i++) {
                sb.append(" ");
            }
            // 이번꺼 출력
            for (int i = start; i <= end; i++) {
                sb.append("-");
                last = end;
            }
            return;
        }

        int centerLen = len / 3;
        int cStart = start + centerLen, cEnd = end - centerLen;
        removeCenter(start, cStart - 1);
        removeCenter(cEnd + 1, end);

    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String line;
        while (((line = br.readLine()) != null)) {
            int N = Integer.parseInt(line);
            int start = 1, end = (int) Math.pow(3, N);
            removeCenter(start, end);
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.close();
        br.close();
    }
}