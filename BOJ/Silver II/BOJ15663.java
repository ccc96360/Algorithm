//BOJ15663 N과 M (9) 20210702
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class BOJ15663 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int m = Integer.parseInt(stk.nextToken());


        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).sorted().toArray();

        HashSet<String> set = new HashSet<>();
        int[] a = {1,2};
        int[] b = {1,2};
        String as = intArrToString(a);
        String bs = intArrToString(b);
        dfs(n,m, 0, arr, new int[m], new HashSet<>(), new HashSet<>());
        bw.flush();
        bw.close();
    }

    public static void dfs(int n, int m, int idx, int[] arr, int[] nums, HashSet<Integer> visited, HashSet<String> visited2){
        if(idx == m){
            String tmp = intArrToString(nums);
            if(!visited2.contains(tmp)){
                visited2.add(tmp);
                System.out.println(tmp);
            }
        }
        else{
            for(int i = 0; i < n; i++){
                if(!visited.contains(i)){
                    nums[idx] = arr[i];
                    visited.add(i);
                    dfs(n, m, idx+1, arr, nums, visited, visited2);
                    visited.remove(i);
                }

            }
        }
    }

    public static String intArrToString(int[] a){
        return Arrays.stream(a).mapToObj(Integer::toString).collect(Collectors.joining(" "));
    }
}