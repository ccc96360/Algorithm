//BOJ1927 최소 힙 20210707
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++){
            int x = Integer.parseInt(br.readLine());
            if(x==0){
                Integer v = pq.poll();
                if(v != null)
                    bw.write(v + "\n");
                else bw.write(0 + "\n");
            }
            else{
                pq.add(x);
            }
        }
        bw.flush();
        bw.close();
    }
}