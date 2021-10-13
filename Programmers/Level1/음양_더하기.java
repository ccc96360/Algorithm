//음양 더하기 월간 코드 챌린지 시즌 2 20211013
class Solution {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        int n = absolutes.length;
        
        for(int i = 0; i < n; i++){
            boolean isPlus = signs[i];
            int v = absolutes[i];
            if(!isPlus) v *= -1;
            answer += v;
            
        }
    
        return answer;
    }
}