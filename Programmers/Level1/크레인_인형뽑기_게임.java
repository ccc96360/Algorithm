import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int n = board.length;
        moves = Arrays.stream(moves).map(x -> x-1).toArray();
        System.out.println(Arrays.toString(moves));
        List<Stack<Integer>> machine = new ArrayList<>();
        for(int c = 0; c < n; c++){
            Stack<Integer> tmp = new Stack<>();
            for(int r = n-1; r >= 0; r--){
                int v = board[r][c];
                if(v != 0){
                    tmp.push(v);
                }
                else break;
            }
            machine.add(tmp);
        }
        Stack<Integer> bucket = new Stack<>();
        bucket.push(-1);
        for(int cmd: moves){
            Stack<Integer> tmp = machine.get(cmd);
            if(!tmp.isEmpty()){
                int v = tmp.pop();
                if(bucket.peek() == v){
                    bucket.pop();
                    answer+=2;
                }
                else{
                    bucket.push(v);
                }
            }
        }
        return answer;
    }
}
