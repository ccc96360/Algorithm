//BOJ1753 최단경로 20210713
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int INF = Integer.MAX_VALUE;

    private static int n,m;
    private static List<List<int[]>> adj;
    private static int[] ans;


    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = nextInt(stk);
        m = nextInt(stk);
        
        int start = Integer.parseInt(br.readLine());
        ans = new int[n+1];
        for(int i = 1; i <= n; i++){
            ans[i] = INF;
        }

        adj = new ArrayList<>();
        for(int i = 0; i <= n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i = 0; i < m; i++){
            stk = new StringTokenizer(br.readLine());
            int u = nextInt(stk), v = nextInt(stk), w = nextInt(stk);
            adj.get(u).add(new int[]{v, w});
        }

        dijkstra(start);
        for(int i = 1; i <= n; i++){
            bw.write(((ans[i] == INF) ? "INF" : ans[i]) + "\n");
        }

        bw.flush();
        bw.close();
    }

    public static void dijkstra(int start){
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x[1]));
        ans[start] = 0;
        pq.add(new int[]{start, 0});

        while(!pq.isEmpty()){
            int[] p = pq.poll();
            int v = p[0], w = p[1];
            if(w > ans[v]) continue;

            for(int[] nv: adj.get(v)){
                if(nv[1] + w < ans[nv[0]]){
                    ans[nv[0]] = nv[1] + w;
                    pq.add(new int[]{nv[0], (nv[1]+w)});
                }
            }
        }
    }

    public static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}