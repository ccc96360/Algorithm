//BOJ11404 플로이드 20210713
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int INF = 100000000;

    private static int n,m;
    private static int[][] floyd;

    public static void main(String[] args) throws IOException {
        n = nextInt();
        m = nextInt();

        floyd = new int[n][n];
        for(int i = 0; i < n; i++) Arrays.fill(floyd[i], INF);

        while(m-- > 0){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int u = nextInt(stk) - 1, v = nextInt(stk) - 1, w = nextInt(stk);
            floyd[u][v] = min(floyd[u][v], w);
        }
        for(int i = 0; i < n; i++) floyd[i][i] = 0;

        for(int k = 0; k < n; k ++){
            for(int i = 0; i < n; i++){
                for(int j = 0; j < n; j++){
                    floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j]);
                }
            }
        }

        for(int[] v: floyd){
            for(int i = 0; i < n - 1; i++){
                bw.write(((v[i] == INF)? 0 : v[i]) + " ");
            }
            bw.write(((v[n-1] == INF)? 0 : v[n-1]) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static int nextInt() throws IOException {
        return Integer.parseInt(br.readLine());
    }

    public static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}