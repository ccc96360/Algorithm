//BOJ5573 산책 20210710
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int h, w, n;
    private static int[][] arr;
    private static int[][] visitedCnt;

    private static int[] dr = {1, 0};
    private static int[] dc = {0, 1};

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        h = Integer.parseInt(stk.nextToken());
        w = Integer.parseInt(stk.nextToken());
        n = Integer.parseInt(stk.nextToken());

        arr = new int[h][w];
        visitedCnt = new int[h][w];
        for(int i = 0; i < h; i++){
            stk = new StringTokenizer(br.readLine());
            for(int j = 0; j < w; j++){
                arr[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        visitedCnt[0][0] = n-1;
        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                int v = visitedCnt[i][j], dir = arr[i][j];
                if(v < 1) continue;
                int a = v / 2;
                int b = (v % 2 == 1)? a + 1 : a;

                int right = (dir == 1)? b : a;
                int down = (dir == 1)? a : b;

                if(i != h - 1) visitedCnt[i + 1][j] += down;
                if(j != w - 1) visitedCnt[i][j + 1] += right;
            }
        }

        for(int i = 0; i < h; i++){
            for(int j = 0; j < w; j++){
                if(visitedCnt[i][j] % 2 == 1) arr[i][j] = (arr[i][j] == 1) ? 0 : 1;
            }
        }
        dfs(new int[]{0,0});
    }

    public static void dfs(int[] v){
        int r = v[0], c = v[1];
        if(r == h || c == w){
            System.out.println((r+1) + " " + (c+1));
            return;
        }
        int dir = arr[r][c];
        dfs(new int[]{r + dr[dir], c+ dc[dir]});
        arr[r][c] = (dir == 0)? 1 : 0;
    }
}