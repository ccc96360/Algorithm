//BOJ9252 LCS2 20210716
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
		
		for(int i = 1; i <= m; i++) {
			for(int j = 1; j <= n; j++) {
				if(b[i-1].equals(a[j-1])) {
					dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j-1]);
				}else {
					dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
				}
			}
			
		}
		
		int tmp = dp[m][n], i = m, j = n;
		String ans = "";
		while(tmp > 0) {
			while(dp[i][j-1] == tmp) {
				j--;
			}
			while(dp[i-1][j] == tmp) {
				i--;
			}
			ans =  a[j-1] + ans;
			tmp--;
			i--; j--;
		}
		if(dp[m][n] == 0) bw.write("0\n");
		else bw.write(dp[m][n] + "\n" + ans);
		bw.flush();
		bw.close();
	}
}
