//BOJ5719 거의 최단 경로 20210713
import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int INF = Integer.MAX_VALUE;

    private static int n,m;
    private static List<List<int[]>> adj;
    private static int[][] canGo;
    private static int[] ans;


    public static void main(String[] args) throws IOException {
        while (true) {
            StringTokenizer stk = new StringTokenizer(br.readLine());
            n = nextInt(stk);
            m = nextInt(stk);
            if(n == 0 && m == 0) break;
            solve();
        }
        bw.flush();
        bw.close();
    }

    public static void solve() throws IOException{
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int start = nextInt(stk);
        int end = nextInt(stk);

        adj = new ArrayList<>();
        canGo = new int[n][n];
        for(int i = 0; i < n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i = 0; i < m; i++){
            stk = new StringTokenizer(br.readLine());
            int u = nextInt(stk), v = nextInt(stk), w = nextInt(stk);
            adj.get(u).add(new int[]{v, w});
            canGo[u][v] = w;
        }

        ans = new int[n];
        dijkstra(start);
        Queue<Integer> q = new LinkedList<>();
        q.add(end);
        while(!q.isEmpty()) {
            int node = q.poll();
            for(int i = 0; i < n; i++){
                if(canGo[i][node] > 0){
                    if(ans[i] == ans[node] - canGo[i][node]){
                        canGo[i][node] = 0;
                        q.add(i);
                    }
                }
            }
        }
        dijkstra(start);
        bw.write(((ans[end] == INF)? -1 : ans[end]) + "\n");
    }
    public static void dijkstra(int start){
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(x -> x[1]));
        Arrays.fill(ans, INF);
        ans[start] = 0;
        pq.add(new int[]{start, 0});

        while(!pq.isEmpty()){
            int[] p = pq.poll();
            int v = p[0], w = p[1];
            if(w > ans[v]) continue;

            for(int[] nv: adj.get(v)){
                if(nv[1] + w < ans[nv[0]] && canGo[v][nv[0]] > 0){
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