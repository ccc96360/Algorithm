//소수 만들기 Summer/Winter Coding(~2018) 20211013
class Solution {
    
    int n;
    int answer = 0;
    public int solution(int[] nums) {
        
        n = nums.length;
        solve(nums, 0, 0, 0);
        
        return answer;
    }
    
    void solve(int[] nums, int depth, int accumulate, int start){
        if(depth == 3){
            if(isPrime(accumulate)){
                answer++;
            }
        }else{
            for(int i = start; i < n; i++){
                accumulate += nums[i];
                solve(nums, depth + 1, accumulate, i + 1);
                accumulate -= nums[i];
                
            }
        }
    }
    
    boolean isPrime(int v){
        if(v < 2) return false;
        for(int i = 3; i <= v - 1; i++){
            if(v % i == 0) return false;
        }
        return true;
    }
}