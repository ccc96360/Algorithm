//BOJ2579 계단 오르기 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int n;
	static int[] arr;
	static int[][] dp;
	
	public static void main(String[] args) throws IOException {
		n = nextInt();
		arr = new int[n];
		
		dp = new int[n][2];
		for(int i = 0; i < n; i++) {
			arr[i] = nextInt();
		}
		
		dp[0][0] = arr[0];
		for(int i = 1; i < n; i++) {
			if(i == 1) {
				dp[1][0] = arr[1];
				dp[1][1] = dp[0][0] + arr[1];
			}else {
				dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + arr[i];
				dp[i][1] = dp[i-1][0] + arr[i];
			}
		}
		
		bw.write(max(dp[n-1][0], dp[n-1][1]) + "\n");
		bw.flush();
		bw.close();
	}
	
	static int nextInt() throws IOException {
		return Integer.parseInt(br.readLine());
	}
}
