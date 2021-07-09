//BOJ1256 사전 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;
    private static int m;
    private static int k;

    private static int INF = 1000000001;
    private static long[][] dp;
    private static String[] ans;


    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());
        k = Integer.parseInt(stk.nextToken());
        dp = new long[n+1][m+1];

        for(int i = 0; i < n+1; i++){
            for(int j = 0; j < m+1; j++){
                dp[i][j] = -1;
            }
        }

        ans = new String[n+m];

        if(getAZ(n,m) < k){
            System.out.println(-1);
        }
        else {
            int cntA = n, cntZ = m;
            for (int i = 0; i < n + m; i++) {
                if(cntA * cntZ == 0){
                    ans[i] = (cntA == 0) ? "z" : "a";
                    continue;
                }
                long tmp = getAZ(cntA - 1, cntZ);
                if(k <= tmp){
                    ans[i] = "a";
                    cntA --;
                }
                else {
                    ans[i] = "z";
                    k -= tmp;
                    cntZ--;
                }
            }
            System.out.println(Arrays.stream(ans).collect(Collectors.joining()));
        }
        bw.flush();
        bw.close();
    }

    public static long getAZ(int a, int z){
        if(a * z == 0){
            return 1;
        }
        if(dp[a][z] != -1){
            return dp[a][z];
        }
        dp[a][z] = getAZ(a - 1, z) + getAZ(a, z - 1);
        if(dp[a][z] > INF){
            dp[a][z] = INF;
        }
        return  dp[a][z];
    }
}