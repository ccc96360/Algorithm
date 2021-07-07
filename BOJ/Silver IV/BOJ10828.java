//BOJ10828 스택 20210707
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int n;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();

        for(int i = 0; i < n; i++){
            String cmd = br.readLine();
            try {
                if (cmd.startsWith("push")) {
                    int v = Integer.parseInt(cmd.split(" ")[1]);
                    stack.push(v);
                } else if (cmd.equals("top")) {
                    bw.write(stack.peek() + "\n");
                } else if (cmd.equals("size")) {
                    bw.write(stack.size() + "\n");
                } else if (cmd.equals("empty")) {
                    bw.write(((stack.isEmpty()) ? 1 : 0) + "\n");
                } else if (cmd.equals("pop")) {
                    bw.write(stack.pop() + "\n");
                }
            }
            catch (Exception e){
                bw.write("-1\n");
            }
        }
        bw.flush();
        bw.close();
    }
}