//땅따먹기 연습문제 20211022
import static java.lang.Math.*;
class Solution {
    int solution(int[][] land) {
        int answer = 0;
        int r = land.length;
        int[][] dp = new int[r][4];
        dp[0] = land[0];
        
        for(int i = 1; i < r; i++){
            int[] prev = dp[i-1];
            dp[i][0] = land[i][0] + max(max(prev[1], prev[2]), prev[3]);
            dp[i][1] = land[i][1] + max(max(prev[0], prev[2]), prev[3]);
            dp[i][2] = land[i][2] + max(max(prev[1], prev[0]), prev[3]);
            dp[i][3] = land[i][3] + max(max(prev[1], prev[2]), prev[0]);
        }

        int[] last = dp[r-1];
        answer = max(max(last[0], last[1]), max(last[2], last[3]));
        return answer;
    }
}