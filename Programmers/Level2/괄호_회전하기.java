//괄호 회전하기 월간 코드 챌린지 시즌 2 20210929
import java.util.*;

class Solution {

    int n;

    public int solution(String s) {
        int answer = 0;
        n = s.length();
        Queue<Character> q = new LinkedList<>();
        for (char c : s.toCharArray()) {
            q.add(c);
        }
        for(int i = 0; i < n-1; i++){
            Queue<Character> nq = new LinkedList<>();
            if(isRight(q, nq)) answer++;
            q = nq;
            rotate(q);
        }
        return answer;
    }

    private void rotate(Queue<Character> q) {
        q.add(q.poll());
    }

    private boolean isRight(Queue<Character> q, Queue<Character> nq) {
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < n; i++){
            Character v = q.poll();
            nq.add(v);

            if(!stack.isEmpty()){
                if(v == '(' || v == '{' || v == '['){
                    stack.push(v);
                }else{
                    Character pop = stack.pop();
                    if((v == ')' && pop != '(')
                            || (v == '}' && pop != '{')
                            || (v == ']' && pop != '[')
                    ) return postProcessing(q, nq);
                }
            }else{
                if(!(v == '(' || v == '{' || v == '[')) return postProcessing(q, nq);
                stack.push(v);
            }
        }
        return stack.isEmpty();
    }
    
    private boolean postProcessing(Queue<Character> q, Queue<Character> nq){
        while (!q.isEmpty()) nq.add(q.poll());
        return false;
    }
}