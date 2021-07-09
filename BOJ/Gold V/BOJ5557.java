//BOJ5557 1학년 20210709
import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;
    private static int[] arr;
    private static long[][] dp;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        dp = new long[n-1][21];
        dp[0][arr[0]] = 1;
        for(int i = 1; i < n-1; i++){
            int v = arr[i];
            for(int j = 0; j <= 20; j++){
                if(dp[i-1][j] > 0){
                    if(j + v <= 20) dp[i][j + v] += dp[i-1][j];
                    if(j - v >= 0) dp[i][j - v] += dp[i-1][j];
                }
            }
        }
        System.out.println(dp[n-2][arr[n-1]]);
    }

}