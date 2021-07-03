//BOJ2075 N번째 큰 수 20210703
import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i ++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            while (stk.hasMoreTokens()){
                pq.add(Integer.parseInt(stk.nextToken()));
            }
        }
        for(int i = 0; i < n-1; i++){
            pq.remove();
        }
        bw.write(pq.poll() + "\n");
        bw.flush();
        bw.close();
    }
}