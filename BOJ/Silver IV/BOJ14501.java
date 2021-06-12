//BOJ14501 퇴사 20210612
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

import static java.lang.Math.max;

public class BOJ14501 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        ArrayList<ArrayList<Integer>> arr = new ArrayList<ArrayList<Integer>>();
        for(int i = 0; i < n; i++){
            ArrayList<Integer> tmp = (ArrayList<Integer>) Arrays.stream(br.readLine().split(" ")).map(Integer::parseInt).collect(Collectors.toList());
            arr.add(tmp);
        }

        int[] dp = new int[n+1];
        for(int day=n-1; day >= 0; day--){
            int t = arr.get(day).get(0);
            int p = arr.get(day).get(1);
            int endDay = day + t - 1;
            dp[day] = dp[day+1];
            if(endDay < n){
                dp[day] = max(p + dp[endDay + 1], dp[day]);
            }
        }
        System.out.println(dp[0]);
    }
}
