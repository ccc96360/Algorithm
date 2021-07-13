//BOJ3830 교수님은 기다리지 않는다. 20210713
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static int[] parent, weight;


    public static void main(String[] args) throws IOException {
        while(true){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            n = nextInt(stk);
            m = nextInt(stk);
            if(n == 0 && m == 0) break;
            solve();
        }

        bw.flush();
        bw.close();
    }

    public static void solve() throws IOException {
        parent = new int[n+1];
        weight = new int[n+1];
        for(int i = 0; i <= n; i++){
            parent[i] = i;
        }
        while(m-- > 0){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            String cmd = stk.nextToken();
            int a = nextInt(stk), b = nextInt(stk);
            if(cmd.equals("!")){
                int w = nextInt(stk);
                union(a, b, w);
            }else{
                int[] resA = find(a), resB = find(b);
                if(resA[0] != resB[0]){
                    bw.write("UNKNOWN" + "\n");
                }
                else{
                    bw.write(resA[1] - resB[1] + "\n");
                }
            }
        }
    }

    public static int[] find(int v){
        if(parent[v] == v){
            return new int[]{v, 0};
        }
        int[] ret = find(parent[v]);
        parent[v] = ret[0];
        ret[1] += weight[v];
        weight[v] = ret[1];
        return ret;
    }

    public static void union(int a, int b, int w){
        int[] aInfo = find(a);
        int[] bInfo = find(b);
        int aRoot = aInfo[0], aWeight = aInfo[1];
        int bRoot = bInfo[0], bWeight = bInfo[1];
        weight[aRoot] = w + bWeight - aWeight;
        parent[aRoot] = bRoot;
    }


    public static int nextInt(StringTokenizer stk){
        return Integer.parseInt(stk.nextToken());
    }
}