//이진 변환 반복하기 월간 코드 챌린지 시즌1 20211007
import java.util.*;

class Solution {
    public int[] solution(String s) {
        int time = 0, deletedZero = 0;
        while(!s.equals("1")){
            Pair<Integer, String> ret = deleteZero(s);
            int cnt = ret.first;
            deletedZero += cnt;
            
            s = ret.second;
            s = Integer.toBinaryString(s.length());
            
            time++;
        }
        
        return new int[]{time, deletedZero};
    }
    
    private Pair<Integer, String> deleteZero(String s){
        StringBuilder sb = new StringBuilder();
        int ret = 0;
        
        for(char v : s.toCharArray()){
            if(v == '1') sb.append(v);
            else ret++;
        }
        
        return new Pair<Integer, String>(ret, sb.toString());
    }
    
    public class Pair<F, S>{
        public F first;
        public S second;
        
        public Pair(F f, S s){
            this.first = f;
            this.second = s;
        }
    }
    
}