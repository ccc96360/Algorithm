//BOJ1932 정수 삼각형 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	private static int n ,k;
	private static int[][] dp = new int[501][501];
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		int[][] triangle = new int[n][];
		for(int i = 0; i < n; i++) {
			triangle[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		}
		
		dp[0][0] = triangle[0][0];
		for(int i = 1; i < n; i++) {
			dp[i][0] = dp[i-1][0] + triangle[i][0];
			dp[i][i] = dp[i-1][i-1] + triangle[i][i];
			for(int j = 1; j < i; j++) {
				dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j];
			}
		}
		bw.write(Arrays.stream(dp[n-1]).max().getAsInt() + "\n");
		bw.flush();
		bw.close();
	}
}
