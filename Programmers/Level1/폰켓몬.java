//폰켓몬 찾아라 프로그래밍 마에스터 20211013
import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int n = nums.length / 2;
        
        Set<Integer> kindOfPhonekemon = new TreeSet<>();
        for(int v : nums){
            kindOfPhonekemon.add(v);
        }    
        
        return (kindOfPhonekemon.size() > n) ? n : kindOfPhonekemon.size();
    }
}