//BOJ3020 개똥벌레 20210708
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> suk = new PriorityQueue<>();
        PriorityQueue<Integer> jong = new PriorityQueue<>();

        int n = Integer.parseInt(stk.nextToken());
        int h = Integer.parseInt(stk.nextToken());

        for(int i = 0; i < n/2; i++){
            suk.add(Integer.parseInt(br.readLine()));
            jong.add(h - Integer.parseInt(br.readLine()));
        }

        int sukSize = suk.size(), jongSize = 0;
        int ans = Integer.MAX_VALUE, cnt = 1;
        for(int lev = 1; lev <= h; lev++){
            while(!suk.isEmpty() && suk.peek() < lev){
                sukSize--;
                suk.poll();
            }
            while(!jong.isEmpty() && jong.peek() < lev){
                jongSize++;
                jong.poll();
            }
            int v = sukSize + jongSize;
            if(v < ans){
                ans = v;
                cnt = 1;
            }
            else if(v==ans){
                cnt++;
            }
        }
        bw.write(ans + " " + cnt + "\n");
        bw.flush();
        bw.close();
    }
}