//BOJ2504 괄호의 값 20210617
import java.io.*;
import java.util.Stack;

public class BOJ2504{
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int solve(String v){
        if(v.length() == 0) return 0;
        int l = 0, r = 0;
        int cnt1 = 0, cnt2 = 0;
        int leftLastIdx = 0;
        int value = (v.charAt(0) == '(')? 2 : 3;
        if(v.length() == 2){
            return value;
        }
        for(int i = 0; i < v.length(); i ++){
            char c = v.charAt(i);
            if(c == '('){
                cnt1++;
            }
            else if(c == '['){
                cnt2++;
            }
            else if(c == ')'){
                cnt1--;
            }
            else{
                cnt2--;
            }
            if(cnt1 == 0 && cnt2 == 0){
                leftLastIdx = i;
                break;
            }
        }
        if(cnt1 != 0 || cnt2 != 0) {
            return 0;
        }

        if(leftLastIdx == v.length()-1){
            l = value * solve(v.substring(1, leftLastIdx));
        }
        else {
            l = solve(v.substring(0, leftLastIdx + 1));
            r = solve(v.substring(leftLastIdx + 1));
        }

        return  l + r;
    }
    private static Boolean isRightString(String v){
        int cnt1 = 0, cnt2 = 0;
        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i < v.length(); i++){
            switch (v.charAt(i)){
                case '(':
                    cnt1++;
                    stack.push(')');
                    break;
                case ')':
                    if(stack.isEmpty() || stack.pop() != ')') return false;
                    cnt1--;
                    break;
                case '[':
                    cnt2++;
                    stack.push(']');
                    break;
                case ']':
                    if(stack.isEmpty() || stack.pop() != ']') return false;
                    cnt2--;
                    break;
            }
        }
        return cnt1 == 0 && cnt2 == 0;
    }
    public static void main(String[] args) throws IOException {
        String str = br.readLine();
        System.out.println((isRightString(str))? solve(str) : 0);
    }
}