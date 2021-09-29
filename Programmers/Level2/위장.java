//위장 코딩테스트 연습 / 해쉬 20210929
import java.util.*;

class Solution {
    
    public int solution(String[][] clothes) {
        Map<String, Integer> map = new HashMap<>();
        
        for (String[] cloth : clothes) {
            String category = cloth[1];
            map.put(category, map.getOrDefault(category, 0) + 1);
        }
        
        return map.values().stream()
                .mapToInt(x -> x + 1)
                .reduce(1, (a, b) -> a * b) - 1;
    }

}