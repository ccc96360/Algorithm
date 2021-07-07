//BOJ2842 집배원 한상덕 20210707
import java.io.*;
import java.util.*;
import java.util.function.Predicate;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int n;
    private static int cntK = 0;
    private static String[][] board;
    private static int[][] arr;
    private static Set<Integer> allHeights;

    private static int[] dr = {-1, 0, 1, 0, -1, -1, 1, 1};
    private static int[] dc = {0, 1, 0, -1, 1, -1, 1, -1};

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        board = new String[n][n];
        arr = new int[n][n];
        allHeights = new HashSet<>();

        for(int i = 0; i < n; i++){
            board[i] = br.readLine().split("");
        }

        for(int i = 0; i < n; i++){
            arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        }

        int[] start = new int[2];
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                allHeights.add(arr[i][j]);
                if(board[i][j].equals("P")){
                    start[0] = i; start[1] = j;
                }
                if(board[i][j].equals("K")){
                    cntK++;
                }
            }
        }

        int[] heights = allHeights.stream().mapToInt(Integer::intValue).sorted().toArray();

        int ans = heights[heights.length-1] - heights[0];
        for(int low = 0, high = 0; low < heights.length & high < heights.length & low <= high;){
            if(bfs(start, heights[low], heights[high]) == cntK){
                ans = min(ans, heights[high] - heights[low]);
                low++;
            }
            else{
                high++;
            }
        }
        bw.write(ans + "\n");
        bw.flush();
        bw.close();
    }

    public static boolean isInRange(int r, int c, int low, int high){
        Predicate<Integer> ret = v -> low <= v && v < high;
        return ret.test(r) && ret.test(c);
    }

    public static int bfs(int[] v, int low, int high){
        if(!isInRange(arr[v[0]][v[1]], arr[v[0]][v[1]], low, high+1)) return 0;
        int cnt = 0;
        boolean[][] visited = new boolean[n][n];
        Queue<int[]> q = new LinkedList<>();
        visited[v[0]][v[1]] = true;
        q.add(v);

        while(!q.isEmpty() && cnt < cntK){
            int[] p = q.poll();
            int r = p[0], c = p[1];
            for(int i = 0; i < 8; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(!isInRange(nr,nc, 0, n)) continue;
                if(!isInRange(arr[nr][nc], arr[nr][nc], low, high+1)) continue;
                if(visited[nr][nc]) continue;

                if(board[nr][nc].equals("K")) cnt++;
                visited[nr][nc] = true;
                q.add(new int[]{nr, nc});
            }
        }

        return cnt;
    }

}