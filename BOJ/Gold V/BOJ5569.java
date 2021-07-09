//BOJ5569 출근 경로 20210709
import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int w,h;
    private static int[][][] dp;
    private static int MOD = 100000;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        h = Integer.parseInt(stk.nextToken());
        w = Integer.parseInt(stk.nextToken());
        dp = new int[h][w][4];

        for(int i = 0; i < h; i++){
            dp[i][0] = new int[]{0, 0, 1, 0};
        }
        for(int i = 0; i < w; i++){
            dp[0][i] = new int[]{1, 0, 0, 0};
        }

        for(int i = 1; i < h; i++){
            for(int j = 1; j < w; j++){
                dp[i][j][0] = (dp[i][j-1][0] + dp[i][j-1][1]) % MOD;
                dp[i][j][1] = dp[i][j-1][2];
                dp[i][j][2] = (dp[i-1][j][2] + dp[i-1][j][3]) % MOD;
                dp[i][j][3] = dp[i-1][j][0];
            }
        }
        System.out.println(Arrays.stream(dp[h-1][w-1]).sum() % MOD);
    }

}