//다음 큰 숫자 연습문제 20211022
import java.util.*;
class Solution {
    public int solution(int n) {
        String s = Integer.toBinaryString(n);
        int m = s.length();
        
        char[] arr = s.toCharArray();
        int idx = 0, cnt = 0;
        boolean changed = false;
        for(int i = m - 1; i >= 1; i--){
            char v = arr[i];
            if(v == '1'){
                if(arr[i-1] == '0'){
                    idx = i;
                    arr[i] = '0';
                    arr[i-1] = '1';
                    changed = true;
                    break;
                }
                cnt++;
            }
        }
        
        String ans = "";
        if(!changed){
            Arrays.fill(arr, '0');
            for(int i = m-1; i >= m - cnt; i--) arr[i] = '1';
            ans = "1" + new String(arr);
        }else{
            for(int i = idx; i < m; i++){
                if(i >= m - cnt) arr[i] = '1';
                else arr[i] = '0';
            }
            ans = new String(arr);
        }
        
        return Integer.parseInt(ans, 2);
    }
}