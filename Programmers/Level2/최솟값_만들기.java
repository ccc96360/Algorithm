//최솟값 만들기 연습문제 20211105
import java.util.*;

class Solution{
    
    public int solution(int []a, int []b){
        int answer = 0, n = a.length;
        Arrays.sort(a);
        Arrays.sort(b);
        for(int i = 0; i < n; i++){
            answer += a[i] * b[n-i-1];
        }
        return answer;
    }
}