//게임 맵 최단거리 찾아라 프로그래밍 마에스터 20210927
import java.util.*;

class Solution {

    int[] dr = new int[]{-1, 0, 1 , 0};
    int[] dc = new int[]{0, 1, 0 , -1};

    public int solution(int[][] maps) {
        return bfs(maps);
    }

    private int bfs(int[][] maps) {
        int n = maps.length, m = maps[0].length;
        boolean[][] visited = new boolean[n][m];
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 1});

        visited[0][0] = true;
        while (!q.isEmpty()){
            int[] tmp = q.poll();
            int r = tmp[0], c = tmp[1], cnt = tmp[2];
            if(r == n-1 && c == m-1){
                return cnt;
            }

            for(int i = 0; i < 4; i++){
                int nr = r + dr[i], nc = c + dc[i];
                if((0 <= nr && nr < n) && 0 <= nc && nc < m){
                    if(!visited[nr][nc] && maps[nr][nc] == 1){
                        visited[nr][nc] = true;
                        q.add(new int[]{nr, nc, cnt + 1});
                    }
                }
            }
        }
        return -1;
    }
}