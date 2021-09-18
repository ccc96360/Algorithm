import java.util.*;
import java.util.stream.*;

import static java.lang.Math.*;
class Solution {
    
    List<List<int[]>> adj = new ArrayList<>();
    boolean[] visited;
    
    public int solution(int n, int[][] costs) {
        int answer = 0;
        for(int i = 0; i < n; i++){
            adj.add(new ArrayList<>());
        }
        for(int[] cost: costs){
            int a = cost[0], b = cost[1], c = cost[2];
            adj.get(a).add(new int[]{b, c});
            adj.get(b).add(new int[]{a, c});
        }
        
        visited = new boolean[n];
        Arrays.fill(visited, false);
        answer = prim();
        return answer;
    }
    
    public int prim(){
        int ret = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> a[1]));
        for(int[] v: adj.get(0)){
            pq.add(v);
        }
        visited[0] = true;
        
        while(!pq.isEmpty()){
            int[] v = pq.poll();
            if(visited[v[0]]) continue;
            visited[v[0]] = true;
            ret += v[1];
            
            for(int[] nv : adj.get(v[0])){
                if(!visited[nv[0]]){
                    pq.add(nv);
                }
            }
        }
        return ret;
    }
}