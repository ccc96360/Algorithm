//카카오프렌즈 컬러링북 2017 카카오코드 예선 20210918
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

class Solution {

    int[] dr = {-1, 0, 1, 0};
    int[] dc = {0, 1, 0, -1};

    int maxR, maxC;

    public int[] solution(int n, int m, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        maxR = n;
        maxC = m;

        boolean[][] visited = new boolean[n][m];

        for(int r = 0; r < n; r++){
            for(int c = 0; c < m; c++){
                if(!visited[r][c] && picture[r][c] != 0){
                    numberOfArea++;
                    maxSizeOfOneArea = max(maxSizeOfOneArea, bfs(r, c, visited, picture[r][c], picture));
                }
            }
        }


        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public int bfs(int r, int c, boolean visited[][], int color, int[][] board){
        int ret = 0;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{r, c});
        visited[r][c] = true;

        while (!q.isEmpty()){
            int[] tmp = q.poll();
            int cr = tmp[0], cc = tmp[1];
            ret++;

            for(int i = 0; i < 4; i++){
                int nr = cr + dr[i], nc = cc + dc[i];
                if((0 <= nr && nr < maxR) && (0 <= nc && nc < maxC)){
                    if(!visited[nr][nc] && board[nr][nc] == color){
                        q.add(new int[]{nr, nc});
                        visited[nr][nc] = true;

                    }
                }
            }
        }

        return ret;
    }
}
