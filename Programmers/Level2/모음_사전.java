//모음 사전 위클리 챌린지 5주차 20211006
import java.util.*;

class Solution {
    public int solution(String word) {
        int answer = 0, idx = 0;
        Map<Character, Integer> toNum = new HashMap<>();
        for(char v : new char[]{'A', 'E', 'I', 'O', 'U'}) toNum.put(v, idx++);
        int[] offset = new int[]{781, 156, 31, 6, 1};
        idx = 0;
        for(char v: word.toCharArray()){
            answer += offset[idx++] * toNum.get(v) + 1;
        }
        return answer;
    }
}