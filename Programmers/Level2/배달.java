import java.util.*;
import java.util.stream.*;

import static java.lang.Math.*;

class Solution {
    
    public List<List<int[]>> adj = new ArrayList<>();
    public int[] distance;
    
    public int solution(int N, int[][] roads, int K) {
        int answer = 0;
        distance = new int[N+1];
        Arrays.fill(distance, Integer.MAX_VALUE);
        for(int i = 0; i <= N; i++){
            adj.add(new ArrayList<>());
        }
        for(int[] road : roads){
            int a = road[0], b = road[1], c = road[2];
            adj.get(a).add(new int[]{b,c});
            adj.get(b).add(new int[]{a,c});
        }

        dijkstra(1);
        for(int v : distance){
            if(v <= K) answer++;
        }
        return answer;
    }
    
    public void dijkstra(int start){
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparing(a -> a[1]));
        distance[start] = 0;
        pq.add(new int[]{start, 0});
        while(!pq.isEmpty()){
            int[] p = pq.poll();
            int v = p[0], w = p[1];
            if(w > distance[v]) continue;
            for(int[] nv : adj.get(v)){
                if(nv[1] + w < distance[nv[0]]){
                    distance[nv[0]] = w + nv[1];
                    pq.add(new int[]{nv[0], nv[1] + w});
                }
            }
        }
    }
}