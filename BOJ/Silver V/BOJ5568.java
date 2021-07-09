//BOJ5568 카드 놓기 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;
    private static int k;
    private static String[] words;


    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        words = new String[n];
        for(int i = 0; i < n; i++){
            words[i] = br.readLine();
        }

        Set<String> selected = new HashSet<>();
        dfs(0, selected, "", new HashSet<>());
        System.out.println(selected.size());
    }

    public static void dfs(int depth, Set<String> selected, String curS, Set<Integer> visitedIdx){
        if(depth == k){
            selected.add(curS);
            return;
        }

        for(int i = 0; i < n; i++){
            if(visitedIdx.contains(i)) continue;
            String tmp = curS;
            tmp += words[i];
            visitedIdx.add(i);
            dfs(depth + 1, selected, tmp, visitedIdx);
            visitedIdx.remove(i);
        }
    }
}