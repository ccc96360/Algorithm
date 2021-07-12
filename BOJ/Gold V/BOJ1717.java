//BOJ1717 집합의 표현 20210712
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static int[] parent;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());

        parent = new int[n+1];
        for(int i = 0; i <= n; i++){
            parent[i] = i;
        }

        for(int i = 0; i < m; i++){
            stk = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(stk.nextToken());
            int b = Integer.parseInt(stk.nextToken());
            int c = Integer.parseInt(stk.nextToken());
            if(a == 0){
                union(b, c);
            }else{
                bw.write(((find(b) == find(c))? "YES" : "NO") + "\n");
            }
        }
        bw.flush();
        bw.close();
    }

    public static int find(int v){
        if(parent[v] == v){
            return v;
        }
        parent[v] = find(parent[v]);
        return parent[v];
    }

    public static void union(int a, int b){
        int ap = find(a);
        int bp = find(b);
        parent[ap] = bp;
    }
}