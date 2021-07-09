//BOJ1010 다리 놓기 20210709
import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;

    public static void main(String[] args) throws IOException {
        int tc = Integer.parseInt(br.readLine());

        int[][] comb = new int[31][31];
        for(int i = 1; i <= 30; i++){
            comb[i][0] = comb[i][i] = 1;
            for(int j = 1; j < i; j++){
                comb[i][j] = comb[i-1][j-1] + comb[i-1][j];
            }
        }
        for(int i = 0; i < tc; i++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(stk.nextToken());
            int n = Integer.parseInt(stk.nextToken());
            bw.write(comb[n][k] + "\n");
        }

        bw.flush();
        bw.close();
    }
}