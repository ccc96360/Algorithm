//BOJ2458 키 순서 20210712
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static int[][] floyd;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());

        floyd = new int[n+1][n+1];

        for(int i = 0; i < m; i++){
            stk = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());

            floyd[a][b] = 1;
        }
        for(int k = 1; k <= n; k++){
            for(int i = 1; i <= n; i++){
                for(int j = 1; j <= n; j++){
                    if(i==j) floyd[i][j] = 1;
                    if(floyd[i][k] == 1 && floyd[k][j] == 1){
                        floyd[i][j] = 1;
                    }
                }
            }
        }

        int ans = 0;
        for(int i = 1; i <= n; i++){
            if(isKnow(i)) ans++;
        }
        System.out.println(ans);
    }
    private static boolean isKnow(int v){
        for(int i = 1; i <= n; i++){
            if(floyd[v][i] != 1 && floyd[i][v] == 0) return false;
        }
        return true;
    }
}