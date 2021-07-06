//BOJ9663 N-Queen 20210706
import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int[][] board;
    private static int n;
    private static int ans = 0;

    private static final int CANT = 1;
    private static final int EMPTY = 2;


    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());

        board = new int[n][n];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                board[i][j] = -1;
            }
        }

        dfs(0);
        System.out.println(ans);

        bw.flush();
        bw.close();
    }

    public static void dfs(int r){
        if(r == n){
            ans ++;
            return;
        }
        for(int c = 0; c < n; c++){
            if(board[r][c] != -1) continue;
            board[r][c] = r;
            makeStatus(r, c, CANT);
            dfs(r+1);
            makeStatus(r, c, EMPTY);
            board[r][c] = -1;
        }

    }
    public static void makeStatus(int r, int c, int status){
        for(int i = 0; i < n; i++){
            if(i == c) continue;
            if(status == CANT) {
                if(board[r][i] == -1) board[r][i] = r;
            }
            else if(status == EMPTY){
                if(board[r][i] == r) board[r][i] = -1;
            }
        }
        for(int i = r+1; i < n; i++){
            if(status == CANT) {
                if(board[i][c] == -1) board[i][c] = r;
            }
            else if(status == EMPTY){
                if(board[i][c] == r) board[i][c] = -1;
            }
        }
        int lc = c-1, rc = c+1;
        for(int i = r+1; i < n; i++){
            if(lc >= 0){
                if(status == CANT) {
                    if(board[i][lc] == -1) board[i][lc] = r;
                }
                else if(status == EMPTY){
                    if(board[i][lc] == r) board[i][lc] = -1;
                }
                lc--;
            }
            if(rc < n){
                if(status == CANT) {
                    if(board[i][rc] == -1) board[i][rc] = r;
                }
                else if(status == EMPTY){
                    if(board[i][rc] == r) board[i][rc] = -1;
                }
                rc++;
            }
        }
    }
}