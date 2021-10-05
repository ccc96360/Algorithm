//전력망을 둘로 나누기 위클리 챌린지 9주차 20211005
import java.util.*;

import static java.lang.Math.*;
class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;
        int m = wires.length;
        for(int i = 0; i < m; i++){
            int[] parent = makeParentArr(n);
            answer = min(answer, solve(parent, i, wires));
        }
        return answer;
    }
    
    private int solve(int[] parent, int except, int[][] wires){
        int n = wires.length;
        for(int i = 0; i < n; i++){
            if(i == except) continue;
            int[] v = wires[i];
            int a = v[0], b = v[1];
            union(a, b, parent);
        }
        for(int i = 1; i < parent.length; i++){
            find(i, parent);
        }
        Map<Integer, Integer> map = new HashMap<>();
        for(int v : parent){
            if(v == 0) continue;
            map.put(v, map.getOrDefault(v, 0) + 1);
        }
        int[] tmp = new int[2];
        int idx = 0;
        for(int key : map.keySet()){
            tmp[idx++] = map.get(key);
        }
        return abs(tmp[0] - tmp[1]);
    }
        
    private int find(int v, int[] parent){
        if(parent[v] != v){
            parent[v] = find(parent[v], parent);
        }
        return parent[v];
    }
    
    private void union(int a, int b, int[] parent){
        int aParent = find(a, parent);
        int bParent = find(b, parent);
        
        parent[bParent] = aParent;
    }
    
    private int[] makeParentArr(int n){
        int[] ret = new int[n+1];
        for(int i = 0; i <= n; i++){
            ret[i] = i;
        }
        return ret;
    }
}