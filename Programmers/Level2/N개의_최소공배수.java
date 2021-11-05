//N개의 최소공배수 연습문제 20211105
import java.util.*;

class Solution {
    public int solution(int[] arr) {
        Arrays.sort(arr);
        
        int lcm = arr[0];
        for(int i = 1; i < arr.length; i++){
            int gcd = gcd(lcm, arr[i]);
            lcm = arr[i] * lcm / gcd;
        }
        
        return lcm;
    }
    
    int gcd(int a, int b){
        if(a % b == 0) return b;
        return gcd(b, a % b);
    }
}