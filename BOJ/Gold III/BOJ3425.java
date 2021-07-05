//BOJ3425 고스택 20210705
import java.io.*;
import java.util.*;

import static java.lang.Math.abs;

public class BOJ3425 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    public static void main(String[] args) throws IOException {
        List<List<String>> commands = new ArrayList<>();
        List<List<Long>> numbers = new ArrayList<>();
        boolean stop = false;
        int cnt = 0;
        while(true){
            List<String> command = new ArrayList<>();;
            List<Long> number = new ArrayList<>();

            while(true){
                String tmp = br.readLine();
                if(tmp.equals("END")){
                    break;
                }
                else if(tmp.equals("QUIT")){
                    stop = true;
                    break;
                }
                else{
                    command.add(tmp);
                }
            }
            if(stop) break;
            Integer n = Integer.parseInt(br.readLine());
            for(int i = 0; i < n; i++){
                number.add(Long.parseLong(br.readLine()));
            }
            commands.add(command);
            numbers.add(number);
            cnt++;
            br.readLine();
        }
        for(int i = 0; i < cnt; i++){
            solve(commands.get(i), numbers.get(i));
        }
        bw.flush();
        bw.close();
    }
    static void solve(List<String> command, List<Long> number) throws IOException {
        for(Long v: number){
            GoStack stack = new GoStack(v);
            boolean hasError = false;
            try {
                for(String cmd: command){
                    if(cmd.equals("POP")){
                        stack.pop();
                    }
                    else if(cmd.equals("INV")){
                        stack.inv();
                    }
                    else if(cmd.equals("DUP")){
                        stack.dup();
                    }
                    else if(cmd.equals("SWP")){
                        stack.swp();
                    }
                    else if(cmd.equals("ADD")){
                        stack.add();
                    }
                    else if(cmd.equals("SUB")){
                        stack.sub();
                    }
                    else if(cmd.equals("MUL")){
                        stack.mul();
                    }
                    else if(cmd.equals("DIV")){
                        stack.div();
                    }
                    else if(cmd.equals("MOD")){
                        stack.mod();
                    }
                    else{
                        String[] tmp = cmd.split(" ");
                        Long num = Long.parseLong(tmp[1]);
                        stack.num(num);
                    }
                }
            }
            catch (Exception e){
                bw.write("ERROR\n");
                hasError = true;
            }

            if(!hasError) {
                if (stack.size() != 1) {
                    bw.write("ERROR\n");
                } else {
                    bw.write(stack.peek() + "\n");
                }
            }
        }
        bw.write("\n");
    }


    static class GoStack{
        Stack<Long> stack = new Stack<>();
        int size = 0;
        public GoStack(Long number) {
            this.stack.push(number);
        }

        public int size(){
            return stack.size();
        }

        public Long peek(){
            return stack.peek();
        }

        public void num(Long v) throws Exception{
            stack.push(v);
        }
        public void pop() throws Exception {
            stack.pop();
        }
        public void inv() throws Exception{
            stack.push(stack.pop() * -1);
        }
        public void dup() throws Exception{
            stack.push(stack.peek());
        }
        public void swp() throws Exception{
            Long first = stack.pop();
            Long second = stack.pop();
            stack.push(first);
            stack.push(second);
        }
        public void add() throws Exception{
            Long first = stack.pop();
            Long second = stack.pop();
            Long ret = first + second;
            if(!isInRange(ret)) throw new Exception();
            stack.push(first + second);
        }
        public void sub() throws Exception{
            Long first = stack.pop();
            Long second = stack.pop();
            Long ret = second - first;
            if(!isInRange(ret)) throw new Exception();
            stack.push(second - first);
        }
        public void mul() throws Exception{
            Long first = stack.pop();
            Long second = stack.pop();
            Long ret = first * second;
            if(!isInRange(ret)) throw new Exception();
            stack.push(first * second);
        }
        public void div() throws Exception{
            Long first = stack.pop();
            Long second = stack.pop();
            boolean isMinus = (first < 0 ) ^ (second < 0);
            first = abs(first);
            second = abs(second);
            Long ret = (second / first) * ((isMinus) ? -1 : 1);
            stack.push(ret);
        }
        public void mod() throws Exception{
            Long first = stack.pop();
            Long second = stack.pop();
            boolean isMinus = second < 0;
            if(isMinus){
                first = abs(first);
                second = abs(second);
                stack.push((second % first) * -1);
            }
            else{
                stack.push(second % first);
            }
        }

        private boolean isInRange(Long n){
            return (-1000000000 <= n && n <= 1000000000);
        }

        @Override
        public String toString() {
            return "GoStack{" +
                    "stack=" + stack +
                    ", size=" + size +
                    '}';
        }
    }
}