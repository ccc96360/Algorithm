//BOJ1516 게임 개발 20210712
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static int[] inDegree;
    private static int[] time;
    private static int[] ans;
    private static List<List<Integer>> adj = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        inDegree = new int[n+1];
        time = new int[n+1];
        ans = new int[n+1];
        for(int i = 0; i <= n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i = 1; i <= n; i++){
            StringTokenizer stk = new StringTokenizer(br.readLine());
            time[i] = Integer.parseInt(stk.nextToken());
            ans[i] = time[i];
            while (true){
                int from = Integer.parseInt(stk.nextToken());
                if(from == -1) break;
                inDegree[i]++;
                adj.get(from).add(i);
            }
        }
        Queue<Integer> q = new LinkedList<>();
        List<Integer> topology = new ArrayList<>();
        for(int i = 1; i <= n; i++){
            if(inDegree[i] == 0){
                q.add(i);
                topology.add(i);
            }
        }
        while(!q.isEmpty()){
            int v = q.poll();
            for(int nv: adj.get(v)){
                inDegree[nv]--;
                if(inDegree[nv] == 0){
                    q.add(nv);
                    topology.add(nv);
                }
            }
        }
        for(int v: topology){
            for(int nv: adj.get(v)){
                ans[nv] = max(ans[v] + time[nv], ans[nv]);
            }

        }
        for(int i = 1; i <= n; i++){
            bw.write(ans[i] + "\n");
        }
        bw.flush();
        bw.close();
    }
}