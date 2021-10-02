//삼각 달팽이 월간 코드 챌린지 시즌1 20211002
import java.util.*;

class Solution {
    
    int [] dr = new int[]{1, 0, -1};
    int [] dc = new int[]{0, 1, -1};
    
    public int[] solution(int n) {
        int[] answer = new int[(n * (n + 1)) / 2];
        
        int[][] arr = new int[n][];
        for(int i = 1; i <= n; i++){
            arr[i - 1] = new int[i];
        }
        
        int dir = 0, m = n - 1, r = 0, c = 0, num = 1;
        while(m >= 0){
            for(int i = 0; i <= m; i++){
                arr[r][c] = num++;
                if(i == m) dir = (dir + 1) % 3;
                r += dr[dir];
                c += dc[dir];
            }
            m--;
        }
        int idx = 0;
        for(int[] v : arr){
            for(int v2 : v){
                answer[idx++] = v2;
            }
        }
        return answer;
    }
}