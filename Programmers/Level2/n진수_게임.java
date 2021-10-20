//n진수 게임 2018 카카오 BLIND RECRUITMENT 20211020
import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(int n, int t, int m, int p) {
        String s = IntStream.rangeClosed(0, t * m)
            .mapToObj(x -> toNBase(x, n))
            .collect(Collectors.joining());
        
        StringBuilder sb = new StringBuilder();
        char[] arr = s.toCharArray();
        int idx = p - 1;
        for(int i = 0; i < t; i++){
            sb.append(String.valueOf(arr[idx]));
            idx += m;
        }
        
        return sb.toString();
    }
    
    String toNBase(int v, int n){
        if(v==0) return "0";
        StringBuilder sb = new StringBuilder();
        while(v != 0){
            int mod = v % n;
            if(mod < 10) sb.append(mod);
            else sb.append(String.valueOf((char)('A' + mod - 10)));
            v /= n;
        }
        sb.reverse();
        return sb.toString();
    }
}



/* Integer.toString(정수, n진법) 으로 진법 변환 기능 제공
import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(int n, int t, int m, int p) {
        String s = IntStream.rangeClosed(0, t * m)
            .mapToObj(x -> Integer.toString(x, n))
            .collect(Collectors.joining());
        
        StringBuilder sb = new StringBuilder();
        char[] arr = s.toCharArray();
        int idx = p - 1;
        for(int i = 0; i < t; i++){
            sb.append(String.valueOf(arr[idx]).toUpperCase());
            idx += m;
        }
        
        return sb.toString();
    }
}
*/