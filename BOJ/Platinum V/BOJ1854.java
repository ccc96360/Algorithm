//BOJ1854 K번째 최단경로 찾기 202107113
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int INF = Integer.MAX_VALUE;

    private static int n,m,k;
    private static List<List<int[]>> adj;
    private static List<PriorityQueue<Integer>> ans;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = nextInt(stk);
        m = nextInt(stk);
        k = nextInt(stk);

        adj = new ArrayList<>();
        for(int i = 0; i <= n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i = 0; i < m; i++){
            stk = new StringTokenizer(br.readLine());
            int u = nextInt(stk), v = nextInt(stk), w = nextInt(stk);
            adj.get(u).add(new int[]{v, w});
        }

        ans = new ArrayList<>();
        for(int i = 0; i <= n ; i++){
            ans.add(new PriorityQueue<>(Comparator.comparingInt(x -> -x)));
            ans.get(i).add(INF);
        }
        dijkstra(1);

        for(int i = 1; i <= n; i++){
            PriorityQueue<Integer> pq = ans.get(i);
            List<Integer> tmp = pq.stream().sorted().collect(Collectors.toList());
            if(tmp.size() < k){
                bw.write(-1 + "\n");
            }else{
                bw.write(tmp.get(k-1) + "\n");
            }
        }
        bw.flush();
        bw.close();
    }
    public static void dijkstra(int start){
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x[1]));
        pq.add(new int[]{start, 0});
        ans.get(start).poll();
        ans.get(start).add(0);

        while(!pq.isEmpty()){
            int[] p = pq.poll();
            int v = p[0], w = p[1];

            PriorityQueue<Integer> vRoutes = ans.get(v);
            int vSize = vRoutes.size();

            if(vSize == k && vRoutes.peek() < w) continue;

            for(int[] nv: adj.get(v)){
                PriorityQueue<Integer> next = ans.get(nv[0]);
                if(nv[1] + w < next.peek() || next.size() < k){
                    if(next.peek() == INF || next.size() == k) next.poll();
                    next.add(nv[1] + w);
                    pq.add(new int[]{nv[0], (nv[1]+w)});
                }
            }
        }
    }

    public static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}