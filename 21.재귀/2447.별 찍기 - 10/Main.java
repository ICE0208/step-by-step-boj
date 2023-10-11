import java.util.Scanner;

public class Main {

    static Character[][] arr;

    static void recur(int n, int rStart, int cStart) {
        if (n == 1) {
            arr[rStart][cStart] = '*';
            return;
        }

        int childN = n / 3;
        for (int rOffset = 0; rOffset < 3; rOffset++) {
            for (int cOffset = 0; cOffset < 3; cOffset++) {
                if (rOffset == 1 && cOffset == 1)
                    continue;

                recur(childN, rStart + childN * rOffset, cStart + childN * cOffset);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());

        arr = new Character[N + 1][N + 1];
        recur(N, 1, 1);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < N + 1; i++) {
            for (int j = 1; j < N + 1; j++) {
                if (arr[i][j] == null) {
                    sb.append(" ");
                } else {
                    sb.append(arr[i][j]);
                }
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());
        sc.close();
    }
}
