import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        String target = br.readLine();
        int targetLen = target.length();

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            stack.push(c);

            while (stack.size() >= targetLen) {
                boolean isSame = true;
                int stackSize = stack.size();

                for (int j = 1; j <= targetLen; j++) {
                    if (stack.get(stackSize - j) == target.charAt(targetLen - j)) {
                        continue;
                    } else {
                        isSame = false;
                        break;
                    }
                }

                if (isSame) {
                    for (int j = 0; j < targetLen; j++) {
                        stack.pop();
                    }
                } else {
                    break;
                }
            }
        }

        if (stack.isEmpty() == false) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < stack.size(); i++) {
                sb.append(stack.get(i));
            }

            bw.write(sb.toString());
        } else {
            bw.write("FRULA");
        }

        bw.close();
        br.close();
    }
}