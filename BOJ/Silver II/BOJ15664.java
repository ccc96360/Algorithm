
//BOJ15664 N과 M (10) 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;
    private static int k;
    private static String[] arr;

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        n = Integer.parseInt(stk.nextToken());
        k = Integer.parseInt(stk.nextToken());

        arr = br.readLine().split(" ");
        Arrays.sort(arr, Comparator.comparingInt(Integer::parseInt));

        dfs(0, 0, "", new HashSet<>(), new HashSet<>());
        bw.flush();
        bw.close();
    }

    public static void dfs(int start, int cnt, String result, Set<String> visited, Set<Integer> visitedIdx) throws IOException {
        if(cnt == k){
            if(!visited.contains(result)){
                visited.add(result);
                bw.write(result + "\n");
            }
            return;
        }
        for(int i = start; i < n; i++){
            if(visitedIdx.contains(i)) continue;
            String tmp = new String(result);
            if(tmp.equals("")) tmp += arr[i];
            else tmp += " " + arr[i];
            visitedIdx.add(i);
            dfs(i + 1, cnt + 1, tmp, visited, visitedIdx);
            visitedIdx.remove(i);
        }
    }
}