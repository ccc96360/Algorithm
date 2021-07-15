//BOJ12865 평범한 배낭 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	private static int n ,k;
	private static List<int[]> items = new ArrayList<int[]>();
	private static int[][] dp;
	
	public static void main(String[] args) throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		n = nextInt(stk);
		k = nextInt(stk);
		dp = new int[n+1][k+1];
		
		for(int i = 0; i < n; i++) {
			stk = new StringTokenizer(br.readLine());
			items.add(new int[] {nextInt(stk), nextInt(stk)});
		}
		
		final Comparator<int[]> comp = (a, b) -> (a[0]==b[0])? Integer.compare(a[1],b[1]) : Integer.compare(a[0], b[0]);
		Collections.sort(items, comp);
		

		for(int i = 1; i <= n; i++) {
			int[] item = items.get(i-1);
			int weight = item[0], value = item[1];
			for(int j = 1; j <= k; j++) {
				if(j < weight) {
					dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
				}else {
					dp[i][j] = max(value + dp[i-1][j-weight], max(dp[i-1][j], dp[i][j-1]));
				}
			}	
		}
		bw.write(dp[n][k] + "\n");
		bw.flush();
		bw.close();
	}
	
	public static int nextInt(StringTokenizer stk) {
		return Integer.parseInt(stk.nextToken());
	}
}
