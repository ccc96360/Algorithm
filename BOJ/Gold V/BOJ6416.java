//BOJ6416 트리 인가? 20210708
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int tc = 1;

        boolean stop = false;
        while (true) {
            List<int[]> info = new ArrayList<>();
            while (true) {
                int u = sc.nextInt();
                int v = sc.nextInt();
                if(u == 0 && v == 0) break;
                if(u < 0 && v < 0){
                    stop = true;
                    break;
                }
                info.add(new int[]{u,v});
            }
            if(stop) break;
            bw.write("Case " + tc++ + " is " + ((isTree(info)) ? "a" : "not a") + " tree.\n");
        }
        bw.flush();
        bw.close();
    }

    public static boolean isTree(List<int[]> info){
        if(info.size() == 0) return true;
        Map<Integer, Integer> inDegree = new HashMap<>();
        Map<Integer, List<Integer>> adj = new HashMap<>();
        Set<Integer> allNodes = new HashSet<>();
        for(int[] connection: info){
            int u = connection[0], v = connection[1];
            allNodes.add(u);
            allNodes.add(v);

            if(!adj.containsKey(u)){
                adj.put(u, new ArrayList<>(Arrays.asList(v)));
            }
            else{
                adj.get(u).add(v);
            }
            if(!inDegree.containsKey(v)){
                inDegree.put(v, 1);
            }else{
                inDegree.put(v, inDegree.get(v) + 1);
            }
        }

        if(allNodes.size() - info.size() != 1) return false;

        int root = -1;
        for(int v: allNodes){
            if(!inDegree.containsKey(v)){
                if(root != -1) return false;
                root = v;
            }else{
                if(inDegree.get(v) > 1) return false;
            }
        }
        if(root == -1) return false;
        Set<Integer> visited = new HashSet<>();
        visited.add(root);
        return dfs(root, adj, visited);
    }

    public static boolean dfs(int v, Map<Integer, List<Integer>> adj, Set<Integer> visited){
        if(adj.containsKey(v)) {
            for (int nv : adj.get(v)) {
                if (visited.contains(nv)) return false;
                visited.add(nv);
                dfs(nv, adj, visited);
                visited.remove(nv);
            }
        }
        return true;
    }
}