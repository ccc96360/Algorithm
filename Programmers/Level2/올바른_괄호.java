//올바른 괄호 연습문제 20211020
import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        for(char c : s.toCharArray()){
            if(c == '('){
                stack.push(c);
           }else{
                if(stack.isEmpty()) return false;
                char top = stack.pop();
                if(top != '(') return false;
            }
        }
        return stack.isEmpty();
    }
}