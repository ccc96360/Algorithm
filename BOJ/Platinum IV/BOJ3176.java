//BOJ3176 도로 네트워크 20210713
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static List<List<int[]>> adj = new ArrayList<>();
    private static int[] depth;
    private static int[][] parent, mn, mx;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        depth = new int[n+1];
        parent = new int[n+1][18];
        mn = new int[n+1][18];
        mx = new int[n+1][18];
        for(int i = 0; i < n + 1; i++){
            adj.add(new ArrayList<>());
        }

        for(int i = 0; i < n - 1; i++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int a = nextInt(stk), b = nextInt(stk), c = nextInt(stk);
            adj.get(a).add(new int[]{b,c});
            adj.get(b).add(new int[]{a,c});
        }

        boolean[] visited = new boolean[n+1];
        Arrays.fill(visited, false);
        dfs(1, visited);

        for(int exp = 1; exp <= 17; exp++){
            for(int node = 1; node <= n; node++){
                parent[node][exp] = parent[parent[node][exp-1]][exp-1];
                mn[node][exp] = min(mn[node][exp-1], mn[parent[node][exp-1]][exp-1]);
                if(mx[parent[node][exp-1]][exp-1] != 0) mx[node][exp] = max(mx[node][exp-1], mx[parent[node][exp-1]][exp-1]);
            }
        }

        m = Integer.parseInt(br.readLine());
        while(m-- > 0){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            int a = nextInt(stk), b = nextInt(stk);
            int[] ans = lca(a,b);
            bw.write(ans[0] + " " + ans[1] + "\n");
        }

        bw.flush();
        bw.close();
    }
    public static int[] lca(int a, int b){
        if(depth[a] > depth[b]){
            int tmp = a;
            a = b; b = tmp;
        }
        int min = mn[b][0], max = mx[b][0];
        for(int exp = 17; exp >= 0; exp--){
            if(depth[b] >= depth[a] + (int) pow(2, exp)){
                min = min(min, mn[b][exp]);
                max = max(max, mx[b][exp]);
                b = parent[b][exp];
            }
        }
        if(a == b) return new int[]{min, max};

        for(int exp = 17; exp >= 0; exp--){
            if(parent[a][exp] != parent[b][exp]){
                min = min(min, min(mn[a][exp], mn[b][exp]));
                max = max(max, max(mx[a][exp], mx[b][exp]));

                a = parent[a][exp];
                b = parent[b][exp];
            }
        }
        min = min(min, min(mn[a][0], mn[b][0]));
        max = max(max, max(mx[a][0], mx[b][0]));
        return new int[]{min, max};
    }


    public static void dfs(int v, boolean[] visited){
        visited[v] = true;
        for(int[] p: adj.get(v)){
            int nv = p[0], w = p[1];

            if(!visited[nv]){
                depth[nv] = depth[v] + 1;
                parent[nv][0] = v;
                mn[nv][0] = w;
                mx[nv][0] = w;
                dfs(nv, visited);
            }
        }
    }

    public static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}