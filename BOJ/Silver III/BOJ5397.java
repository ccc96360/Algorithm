//BOJ5397 키로거 20210701

import java.io.*;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int tc = Integer.parseInt(br.readLine());
        for(int i = 0; i < tc; i++){
            bw.write(solve() + "\n");
        }

        bw.flush();
        bw.close();
    }

    public static String solve() throws IOException{
        String[] keyLog = br.readLine().split("");
        Stack<String> left = new Stack<>();
        Stack<String> right = new Stack<>();
        for(String v: keyLog){
            if(v.equals("<")){
                if(!left.isEmpty())
                    right.push(left.pop());
            }
            else if(v.equals(">")){
                if(!right.isEmpty())
                    left.push(right.pop());
            }
            else if(v.equals("-")){
                if(!left.isEmpty())
                    left.pop();
            }
            else{
                left.push(v);
            }
        }

        while(!right.isEmpty()){
            left.push(right.pop());
        }

        return left.stream().collect(Collectors.joining());
    }

}