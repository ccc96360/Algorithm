//문자열 압축 2020KAKAO BLIND RECRUITMENT 20211107
import static java.lang.Math.*;

class Solution {
    public int solution(String s) {
        int n = s.length();
        int answer = n;
        char[] arr = s.toCharArray();
        for(int k = 1; k <= n; k++){
            int offset = 0, cnt = 1;
            
            String prev = new String(arr, offset, k);
            StringBuilder sb = new StringBuilder();
            offset += k;
            
            while(offset + k <= n){
                String str = new String(arr, offset, k);
                if(prev.equals(str)){
                    cnt += 1;
                }else{
                    if(cnt != 1) sb.append(cnt);
                    sb.append(prev);
                    cnt = 1;
                }
                prev = str;
                offset += k;
            }
            if(cnt != 1) sb.append(cnt);
            sb.append(prev);
            
            if(offset != n){
                sb.append(new String(arr, offset, n - offset));
            }
            answer = min(answer, sb.toString().length());
        }
    
        return answer;
    }
}