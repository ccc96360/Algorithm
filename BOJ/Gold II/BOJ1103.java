//BOJ1103 게임 20210705
import java.io.*;
import java.util.*;

import static java.lang.Math.max;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int n,m;
    private static String[][] board;
    private static int[][] visited;
    private static int[][] dp;


    private static int[] dr = {-1,0,1,0};
    private static int[] dc = {0,1,0,-1};

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());

        board = new String[n][m];
        visited = new int[n][m];
        dp = new int[n][m];

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                dp[i][j] = -1;
            }
        }

        for(int i = 0; i < n; i++){
            board[i] = br.readLine().split("");
        }

        System.out.println(dfs(new int[]{0,0}, 0));
    }

    static int dfs(int[] v, int depth){
        int r = v[0], c = v[1];
        if(!((0 <= r && r < n) && (0 <= c && c < m)) || board[r][c].equals("H"))
            return depth;

        if(visited[r][c] != 0){
            return -1;
        }
        if(dp[r][c] >= depth) return 0;
        dp[r][c] = depth;
        visited[r][c] = depth;
        int amount = Integer.parseInt(board[r][c]);
        int ret = Integer.MIN_VALUE;
        for(int i = 0; i < 4; i++) {
            int nr = r + dr[i] * amount;
            int nc = c + dc[i] * amount;

            int dfs = dfs(new int[]{nr,nc}, depth + 1);
            if(dfs == -1){
                return -1;
            }
            ret = max(dfs, ret);
        }
        visited[r][c] = 0;
        return ret;
    }
}