//BOJ7579 앱 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	static int n, m;
	static int[] memories, costs;
	static int[][] dp;
	public static void main(String[] args) throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		n = nextInt(stk);
		m = nextInt(stk);
		
		memories = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		costs = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		
		dp = new int[n+1][10001];
		for(int i = 1; i <= n; i++) {
			int memory = memories[i-1], cost = costs[i-1];
			for(int j = 0; j <= 10000; j ++) {
				if(cost > j) {
					dp[i][j] = dp[i-1][j];
				}else {
					dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + memory);
				}
			}
		}
		int ans = 0;
		for(int cost = 0; cost <= 10000 && ans == 0; cost++) {
			for(int i = 1; i <= n; i++) {
				if(dp[i][cost] >= m) {
					ans = cost;
					break;
				}
			}
		}
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
		
	}
	
	static int nextInt(StringTokenizer stk){
		return Integer.parseInt(stk.nextToken());
	}
}
