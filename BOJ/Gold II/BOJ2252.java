//BOJ2252 줄 세우기 20210712
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static int[] inDegree;
    private static List<List<Integer>> adj = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        m = Integer.parseInt(stk.nextToken());

        inDegree = new int[n+1];
        for(int i = 0; i <= n; i++) {
            adj.add(new ArrayList<>());
        }
        for(int i = 0; i < m; i++){
           stk = new StringTokenizer(br.readLine());
           int a = Integer.parseInt(stk.nextToken());
           int b = Integer.parseInt(stk.nextToken());
           inDegree[b]++;
           adj.get(a).add(b);
        }

        List<Integer> ans = topologySort();
        System.out.println(ans.stream().map(v -> Integer.toString(v)).collect(Collectors.joining(" ")));
        bw.flush();
        bw.close();
    }

    public static List<Integer> topologySort(){
        List<Integer> topology = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        for(int i = 1; i <= n; i++){
            if(inDegree[i] == 0){
                q.add(i);
            }
        }
        while(!q.isEmpty()){
            int v = q.poll();
            topology.add(v);
            for(int nv : adj.get(v)){
                inDegree[nv]--;
                if(inDegree[nv] == 0){
                    q.add(nv);
                }
            }
        }
        return topology;
    }
}