//BOJ5582 공통 부분 문자열 20210716
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	static int n, m;
	static int[][] dp;
	public static void main(String[] args) throws IOException {
		String[] a = br.readLine().split("");
		String[] b = br.readLine().split("");
		
		n = a.length; m = b.length;
		dp = new int[m+1][n+1];
		
		int ans = 0;
		for(int i = 1; i <= m; i++) {
			for(int j = 1; j <= n; j++) {
				if(b[i-1].equals(a[j-1])) {
					dp[i][j] = dp[i-1][j-1] + 1;
					ans = max(ans, dp[i][j]);
				}
			}
			
		}
		
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
	}
}
