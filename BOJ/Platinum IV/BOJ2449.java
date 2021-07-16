//BOJ2449 전구 20210716
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	static int n, k;
	static int[] arr;
	static int[][] dp;
	public static void main(String[] args) throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		n = nextInt(stk); k = nextInt(stk);
		
		dp = new int[n][n];
		for(int i = 0; i < n; i++) Arrays.fill(dp[i], -1);
		arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

		bw.write(solve(0, n-1) + "\n");
		bw.flush();
		bw.close();
	}
	
	static int solve(int s, int e) {
		if(s == e) return 0;
		if(dp[s][e] != -1) return dp[s][e];
		
		int mn = Integer.MAX_VALUE;
		for(int i = s; i < e; i++) {
			mn = min(mn, solve(s, i) + solve(i + 1, e) + ((arr[s] == arr[i+1])? 0:1));
		}
		dp[s][e] = mn;
		return dp[s][e];
	}
	static int nextInt(StringTokenizer stk) {
		return Integer.parseInt(stk.nextToken());
	}
}
