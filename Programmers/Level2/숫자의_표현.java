//숫자의 표현 연습문제 20211105
class Solution {
    public int solution(int n) {
        int answer = 0, sum = 0;
        int left = 1, right = 1;
        while(left <= n){
            if(sum < n){
                sum += right++;
            }else if(sum > n){
                sum -= left++;
            }else{
                answer++;
                sum -= left++;
            }
        }
        return answer;
    }
}