//BOJ2529 부등호 20210702
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class BOJ2529 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static String min = "9999999999";
    private static String max = "0000000000";

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        String[] bu = br.readLine().split(" ");

        for(int i = 0; i <= 9; i++){
            int[] tmp = new int[n+1];
            HashSet<Integer> visited = new HashSet<>();

            tmp[0] = i;
            visited.add(i);
            dfs(i, 0, n, bu, tmp, visited);
            visited.remove(i);

        }

        bw.write(max + "\n" + min);
        bw.flush();
        bw.close();
    }
    public static void dfs(int curN, int idx, int n, String[] bu, int[] nums, HashSet<Integer> visited){
        if(idx == n){
            String ret = Arrays.stream(nums).mapToObj(Integer::toString).collect(Collectors.joining());
            if(ret.compareTo(min) < 0){
                min = ret;
            }
            else if(ret.compareTo(max) > 0){
                max = ret;
            }
        }
        else {
            for (int i = 0; i <= 9; i++) {
                if (!visited.contains(i) && isRight(curN, i, bu[idx])) {
                    visited.add(i);
                    nums[idx+1] = i;
                    dfs(i, idx + 1, n, bu, nums, visited);
                    visited.remove(i);
                }
            }
        }
    }

    public static Boolean isRight(int curN, int nextN, String bu){
        if(bu.equals("<")){
            return curN < nextN;
        }
        else{
            return curN > nextN;
        }
    }
}