//주식 가격 코딩테스트 연습 / 스택/큐 20211002
import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] answer = new int[n];
        Stack<int[]> stack = new Stack<>();
        
        stack.push(new int[]{prices[0], 0});
        for(int i = 1; i < n; i ++){
            int price = prices[i];
            
            
            while(!stack.isEmpty() && price < stack.peek()[0]){
                int[] pop = stack.pop();
                answer[pop[1]] = i - pop[1];
            }
            stack.push(new int[]{price, i});
            
        }
        while(!stack.isEmpty()){
            int[] pop = stack.pop();
            answer[pop[1]] = n - 1 - pop[1];
        }
        return answer;
    }
}