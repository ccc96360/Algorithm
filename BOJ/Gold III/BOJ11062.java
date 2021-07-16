//BOJ11062 카드 게임 20210716
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
		int tc = Integer.parseInt(br.readLine());
		while(tc-- > 0) solve();
		bw.flush();
		bw.close();
	}
	
	static void solve() throws IOException{
		n = Integer.parseInt(br.readLine());
		dp = new int[n][n];
		for(int[] v: dp) Arrays.fill(v, -1);
		
		arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		bw.write(maxScore(0, n -1) + "\n");
	}
	
	static int maxScore(int s, int e) {
		if(s > e) return 0;
		if(dp[s][e] != - 1) return dp[s][e];
		if(e == s) return arr[s];
		if(e - s == 1) {
			dp[s][e] = max(arr[s], arr[e]);
			return dp[s][e];
		}
		
		int left = arr[s] + min(maxScore(s+2, e), maxScore(s+1, e-1));
		int right = arr[e] + min(maxScore(s, e-2), maxScore(s+1, e-1));
		dp[s][e] = max(left, right);
		return dp[s][e];
	}
}
