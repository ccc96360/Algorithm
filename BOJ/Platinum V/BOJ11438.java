//BOJ11438 LCA 2 20210712
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static List<List<Integer>> adj = new ArrayList<>();
    private static int[] depth;
    private static int[][] parent;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        depth = new int[n+1];
        parent = new int[n+1][18];
        for(int i = 0; i <= n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i = 0; i < n-1; i ++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());

            adj.get(a).add(b);
            adj.get(b).add(a);
        }

        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);
        dfs(1, visited);

        //parent[][exp] => 2 ^ exp 위의 조상
        for(int exp = 1; exp <= 17; exp++){
            for(int node = 1; node <= n; node++){
                parent[node][exp] = parent[parent[node][exp-1]][exp-1];
            }
        }

        m = Integer.parseInt(br.readLine());
        while (m-- > 0){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());
            bw.write(lca(a,b) + "\n");
        }

        bw.flush();
        bw.close();
    }

    public static int lca(int a, int b){
        if(depth[a] > depth[b]){
            int tmp = a;
            a = b; b = tmp;
        }
        for(int exp = 17; exp >= 0; exp--){
            if(depth[b] >= depth[a] + (int) pow(2, exp)){
                b = parent[b][exp];
            }
        }
        if(a == b) return a;

        for(int exp = 17; exp >= 0; exp--){
            if(parent[a][exp] != parent[b][exp]){
                a = parent[a][exp];
                b = parent[b][exp];
                break;
            }
        }
        return parent[a][0];
    }

    public static void dfs(int v, boolean[] visited){
        visited[v] = true;
        for(int nv: adj.get(v)){
            if(!visited[nv]){
                depth[nv] = depth[v] + 1;
                parent[nv][0] = v;
                dfs(nv, visited);
            }
        }
    }
}