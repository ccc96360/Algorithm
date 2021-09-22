//짝지어 제거하기 2017 팁스타운 20210922
import java.util.*;

class Solution {
    public int solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (Character v : s.toCharArray()) {
            if(stack.isEmpty() || !stack.peek().equals(v)){
                stack.add(v);
            }else if(stack.peek().equals(v)){
                stack.pop();
            }
        }

        return (stack.isEmpty())? 1 : 0;
    }

}