//BOJ11266 단절점 20210719
import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    static int n, m, cnt = 0;
    static List<List<Integer>> adj = new ArrayList<>();
    static int[] ord, children;
    static boolean[] isCutVertex;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = nextInt(stk); m = nextInt(stk);
        ord = new int[n+1]; children = new int[n+1]; isCutVertex = new boolean[n+1];

        for(int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for(int i = 0; i < m; i++){
            stk = new StringTokenizer(br.readLine());
            int u = nextInt(stk), v = nextInt(stk);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        for(int i = 1; i <= n; i++){
            if(ord[i] == 0){
                dfs(i);
                isCutVertex[i] = children[i] >= 2;
            }
        }
        long cnt = IntStream.rangeClosed(1,n).filter(x -> isCutVertex[x]).count();
        bw.write(cnt + "\n");
        for(int i = 1 ; i <= n; i++){
            if (isCutVertex[i]){
                bw.write(i + " ");
            }
        }
        bw.write("\n");
        bw.flush();
        bw.close();
    }

    static int dfs(int v){
        ord[v] = ++cnt;
        int ret = ord[v];

        int child = 0;
        for(int nv: adj.get(v)){
            if(ord[nv] == 0){
                int low = dfs(nv);
                child++;
                if(low >= ord[v]){
                    isCutVertex[v] = true;
                }
                ret = min(ret, low);
            }else{
                ret = min(ret, ord[nv]);
            }
        }
        children[v] = child;
        return ret;
    }



    static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}