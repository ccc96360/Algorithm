//BOJ1655 가운데를 말해요 20210707
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;

    public static void main(String[] args) throws IOException {
        PriorityQueue<Integer> minQ = new PriorityQueue<>();
        PriorityQueue<Integer> maxQ = new PriorityQueue<>((o1, o2) -> Integer.compare(o2, o1));

        n = Integer.parseInt(br.readLine());
        for(int cnt = 1; cnt <= n; cnt++){
            int v = Integer.parseInt(br.readLine());

            if(maxQ.size() == minQ.size()){
                maxQ.add(v);
            }
            else{
                minQ.add(v);
            }
            if(!maxQ.isEmpty() && !minQ.isEmpty() && maxQ.peek() > minQ.peek()){
                int mx = maxQ.poll(), mn = minQ.poll();
                maxQ.add(mn);
                minQ.add(mx);
            }
            bw.write(maxQ.peek() + "\n");
        }
        bw.flush();
        bw.close();
    }
}