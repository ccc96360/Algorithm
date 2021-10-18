//가장 큰 정사긱형 찾기 연습문제 20211018
import java.util.*;

import static java.lang.Math.*;
class Solution{
    
    int[] dr = {-1, -1, 0};
    int[] dc = {-1, 0, -1};
    int n,m;
    public int solution(int [][]board){
        int answer = 0;

        n = board.length;
        m = board[0].length;
        
        int[][] dp = new int[n][m];
        
        for(int r = 0; r < n; r++){
            for(int c = 0; c < m; c++){
                if(board[r][c] == 0) continue;
                if(r == 0 || c == 0){
                    dp[r][c] = 1;
                }else{
                    int mn = 1001;
                    for(int i = 0; i < 3; i++){
                        int nr = r + dr[i], nc = c + dc[i];
                        if(0 <= nr && nr < n && 0 <= nc && nc < m){
                            mn = min(dp[nr][nc], mn);
                        }
                    }
                    dp[r][c] = mn + 1;
                }
                answer = max(dp[r][c], answer);
            }
        }
        return answer * answer;
    }
    
}