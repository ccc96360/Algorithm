//영어 끝말잇기 Summer/Winter Coding(~2018) 20211002
import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int maxTurn = words.length / n;
        
        Set<String> history = new TreeSet<>();
        String lastWord = "";
        for(int turn = 1; turn <= maxTurn; turn++){
            for(int person = 1; person <= n; person++){
                int offset = ((turn - 1) * n) + person - 1;
                String word = words[offset];
                if(offset != 0 && lastWord.charAt(lastWord.length() - 1) != word.charAt(0)){
                    return new int[]{person, turn};
                }
                if(history.contains(word)){
                    return new int[]{person, turn};
                }
                history.add(word);
                lastWord = word;
            }
        }
        return new int[]{0, 0};
    }
}