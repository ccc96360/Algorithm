//BOJ1922 네트워크 연결 20210712
import java.io.*;
import java.util.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static List<List<int[]>> adj = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        for(int i = 0; i <= n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i = 0; i < m; i++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());
            int c = Integer.parseInt(stk.nextToken());
            adj.get(a).add(new int[]{b,c});
            adj.get(b).add(new int[]{a,c});
        }
        boolean[] visited = new boolean[n+1];
        
        Comparator<int[]> comp = Comparator.comparingInt(a -> a[1]);
        PriorityQueue<int[]> pq = new PriorityQueue<>(comp);
        for(int[] v: adj.get(1)){
            pq.add(v);
        }
        visited[1] = true;
        
        int ans = 0;
        while(!pq.isEmpty()){
            int[] v = pq.poll();
            if(visited[v[0]]) continue;
            visited[v[0]] = true;
            ans += v[1];
            for(int[] nv: adj.get(v[0])){
                if (!visited[nv[0]]){
                    pq.add(nv);
                }
            }
        }
        System.out.println(ans);
    }
}