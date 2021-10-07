//점프와 순간 이동 Summer/Winter Coding(~2018) 20211007

public class Solution {
    public int solution(int n) {
        int ans = 0;
        
        while(n != 0){
            if(n % 2 == 1){
                ans++;
                n--;
            } 
            n /= 2;
        }
        return ans;
    }
}