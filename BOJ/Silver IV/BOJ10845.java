//BOJ10845 큐 20210612
import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class BOJ10845 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        Deque<Integer> dq = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++ ){
            String[] s =  br.readLine().split(" ");
            Integer x;
            switch (s[0]){
                case "push":
                    x = Integer.parseInt(s[1]);
                    dq.addLast(x);
                    break;
                case "pop":
                    if((x = dq.pollFirst()) == null){
                        x = -1;
                    }
                    bw.write(x + "\n");
                    break;
                case "size":
                    bw.write(dq.size() + "\n");
                    break;
                case "empty":
                    x = (dq.isEmpty()) ? 1 : 0;
                    bw.write(x + "\n");
                    break;
                case "front":
                    x = (dq.isEmpty()) ? -1 : dq.getFirst();
                    bw.write(x + "\n");
                    break;
                case "back":
                    x = (dq.isEmpty()) ? -1 : dq.getLast();
                    bw.write(x + "\n");
                    break;
            }
        }
        bw.flush();
        bw.close();

    }
}
