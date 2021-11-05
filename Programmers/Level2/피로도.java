//피로도 위클리 챌린지 20211105
import java.util.*;

import static java.lang.Math.*;

class Solution {
    int n, answer;
    int[][] dungeons;
    public int solution(int k, int[][] ds) {        
        answer = -1;
        n = ds.length;
        dungeons = ds;
        
        solve(0, k, new boolean[n]);
        
        return answer;
    }
    
    public void solve(int depth, int leftEnergy, boolean[] selected){
        answer = max(answer, depth);
        for(int i = 0; i < n; i++){
            if(selected[i]) continue;
            int[] dungeon = dungeons[i];
            if(dungeon[0] <= leftEnergy){
                selected[i] = true;
                solve(depth + 1, leftEnergy - dungeon[1], selected);
                selected[i] = false;
            }   
        }
    }
}