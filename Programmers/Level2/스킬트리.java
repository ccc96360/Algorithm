//스킬트리 Summer/Winter Coding(~2018) 20211009
import java.util.*;
class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = skill_trees.length;
        
        Map<Character, Integer> nice = new HashMap<>();
        int idx = 1;
        for(char v : skill.toCharArray()){
            nice.put(v, idx++);
        }
        
        for(String s : skill_trees){
            int curNice = 1;
            for(char v : s.toCharArray()){
                if(!nice.containsKey(v)) continue;
                if(nice.get(v) != curNice){
                    answer--;
                    break;
                }
                curNice++;
            }
        }
        
        return answer;
    }
}