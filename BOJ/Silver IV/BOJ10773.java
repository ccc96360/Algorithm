//BOJ10773 제로 20210614
import java.io.*;
import java.util.*;

public class BOJ10773 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(0);
        for(int i = 0; i < n; i++){
            int t = Integer.parseInt(br.readLine());
            if(t == 0){
                stack.pop();
            }
            else{
                stack.push(t);
            }
        }
        System.out.println(stack.stream().reduce(0, Integer::sum));
    }
}