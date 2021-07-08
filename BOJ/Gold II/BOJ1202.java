//BOJ1202 보석 도둑 20210708
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int k = Integer.parseInt(stk.nextToken());
        List<int[]> gems = new ArrayList<>();
        for(int i = 0; i < n; i++){
            gems.add(Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray());
        }
        Collections.sort(gems, Comparator.comparingInt(a -> a[0]));

        int[] bags = new int[k];
        for(int i = 0; i < k; i++){
            bags[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(bags);

        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> Integer.compare(b,a));
        int idx = 0;
        long ans = 0;
        for(int bag: bags){
            while(idx < n && bag >= gems.get(idx)[0]){
                pq.add(gems.get(idx)[1]);
                idx += 1;
            }
            if(!pq.isEmpty()) ans += pq.poll();
        }
        bw.write(ans + "\n");
        bw.flush();
        bw.close();
    }
}