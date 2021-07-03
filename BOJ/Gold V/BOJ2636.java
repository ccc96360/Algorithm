//BOJ2636 치즈 20210703
import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int[] dr = {-1, 0, 1, 0};
    static int[] dc = {0, 1, 0, -1};

    static int n;
    static int m;
    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());

        int[][] arr = new int[n][m];
        int cheeseCnt = 0;
        for(int r = 0; r < n; r++){
            stk = new StringTokenizer(br.readLine());
            for(int c = 0; c < m; c++){
                arr[r][c] = Integer.parseInt(stk.nextToken());
                if(arr[r][c] == 1) cheeseCnt++;
            }
        }
        List<int[]> edges = findEdge(arr);
        int ans = cheeseCnt, time = 0;
        while (!edges.isEmpty()){
            int deletedCheese = 0;

            for(int[] edge : edges){
                int r = edge[0];
                int c = edge[1];
                arr[r][c] = 0;
                deletedCheese++;
            }
            edges = findEdge(arr);
            time++;
            ans = deletedCheese;
        }
        bw.write(time + "\n" + ans);
        bw.flush();
        bw.close();
    }


    static List<int[]> findEdge(int[][] arr){
        List<int[]> edges = new ArrayList<>();
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> q = new LinkedList<>();
        visited[0][0] = true;
        q.add(new int[]{0,0});

        while (!q.isEmpty()){
            int[] point = q.poll();
            int r = point[0];
            int c = point[1];
            for(int i = 0; i < 4; i++){
                int nr = r + dr[i];
                int nc = c + dc[i];
                if(0 <= nr && nr < n && 0 <= nc && nc < m){
                    if(!visited[nr][nc]){
                        visited[nr][nc] = true;
                        if(arr[nr][nc] == 0) q.add(new int[]{nr,nc});
                        else{
                            edges.add(new int[]{nr, nc});
                        }
                    }
                }
            }
        }

        return edges;
    }
}