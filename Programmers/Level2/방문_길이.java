//방문 길이 Summer/Winter Coding(~2018) 20211009
import java.util.*;
class Solution {
    int[] dx = {0, 1, 0, -1}; // UP, RIGHT, DOWN, LEFT
    int[] dy = {1, 0, -1, 0};
    
    public int solution(String dirs) {
        int answer = 0;
        int fx = 5, fy = 5;
        boolean[][][][] line = new boolean[11][11][11][11];
        Map<Character, Integer> dirToIdx =  makeDirToIdxMap();
        
        for(char v : dirs.toCharArray()){
            int dir = dirToIdx.get(v);
            int tx = fx + dx[dir], ty = fy + dy[dir];
            if(!(0 <= tx && tx <= 10)) continue;
            if(!(0 <= ty && ty <= 10)) continue;
            if(!line[fx][fy][tx][ty]){
                answer++;
            }
            line[fx][fy][tx][ty] = true;
            line[tx][ty][fx][fy] = true;
            fx = tx;
            fy = ty;
        }
        
        return answer;
    }
    
    private Map<Character, Integer> makeDirToIdxMap(){
        Map<Character, Integer> ret =  new HashMap<>();
        ret.put('U', 0);
        ret.put('R', 1);
        ret.put('D', 2);
        ret.put('L', 3);
        return ret;
        
    }
}