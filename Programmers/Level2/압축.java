//압축 2018 카카오 BLIND RECRUITMENT 20211019
import java.util.*;

class Solution {
    
    public int[] solution(String msg) {
        int n = msg.length();
        List<Integer> ans = new ArrayList<>();
        Dictionary dict = new Dictionary();
        
        char[] msgArr = msg.toCharArray();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++){
            char c = msgArr[i];
            if(dict.hasWord(sb.toString() + String.valueOf(c))){
                sb.append(c);
            }else{
                ans.add(dict.getIdx(sb.toString()));
                sb.append(c);
                dict.add(sb.toString());
                sb = new StringBuilder(String.valueOf(c));
            }
        }
        if(!"".equals(sb.toString())){
            ans.add(dict.getIdx(sb.toString()));
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
    
    
    class Dictionary{
        Map<String, Integer> info = new TreeMap<>();
        int lastIdx = 1;
        
        Dictionary(){
            for(char c = 'A'; c <= 'Z'; c++){
                info.put(String.valueOf(c), lastIdx++);
            }
        }
        
        void add(String v){
            info.put(v, lastIdx++);
        }
        
        int getIdx(String v){
            return info.get(v);
        }
        
        boolean hasWord(String v){
            return info.containsKey(v);
        }
        Map<String, Integer> getInfo(){ return info; }
    }
}