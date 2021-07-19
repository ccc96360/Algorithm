//BOJ11400 단절선 20210719
import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int n, m, cnt = 0;
    static List<List<Integer>> adj = new ArrayList<>();
    static List<int[]> res = new ArrayList<>();
    static int[] ord;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = nextInt(stk); m = nextInt(stk);
        ord = new int[n+1];

        for(int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for(int i = 0; i < m; i++){
            stk = new StringTokenizer(br.readLine());
            int u = nextInt(stk), v = nextInt(stk);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        dfs(1, 0);
        Comparator<int[]> comp = (a,b) -> (a[0]==b[0]) ? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]);
        Collections.sort(res, comp);
        bw.write(res.size() + "\n");
        for(int[] v: res){
            bw.write(v[0] + " " + v[1] + "\n");
        }
        bw.flush();
        bw.close();
    }

    static int dfs(int v, int parent){
        ord[v] = ++cnt;
        int ret = ord[v];

        for(int nv: adj.get(v)){
            if(nv == parent) continue;
            if(ord[nv] == 0){
                int low = dfs(nv, v);
                if(low > ord[v]){
                    res.add(new int[]{min(v,nv), max(v, nv)});
                }
                ret = min(ret, low);
            }else{
                ret = min(ret, ord[nv]);
            }
        }
        return ret;
    }



    static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}