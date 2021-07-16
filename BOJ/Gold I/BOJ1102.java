//BOJ1102 발전소 20210716
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	static int n, p, INF = Integer.MAX_VALUE;
	static int[][] arr;
	static String[] status;
	static int[] dp;
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		arr = new int[n][n];
		dp = new int[1<<(n+1)];
		Arrays.fill(dp, INF);
		for(int i = 0; i < n; i++) {
			arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		}
		
		status = br.readLine().split("");
		p = Integer.parseInt(br.readLine());
		int aliveFactory = 0;
		for(int i = 0; i < n; i++) {
			if(status[i].equals("Y")) {
				aliveFactory |= 1 << i;
			}
		}
		
		Queue<int[]> q = new LinkedList<>();
		int v = aliveFactory;
		q.add(new int[] {v, 0});
		dp[v] = 0;
		while(!q.isEmpty()) {
			int[] p = q.poll();
			v = p[0];
			int w = p[1];
			if(w > dp[v]) continue;
			for(int to = 0; to < n ; to ++) {
				int nv = 1 << to;
				if((nv & v) > 0)  continue;
				
				nv |= v;
				for(int from = 0; from < n; from++) {
					if(((1 << from) & nv) > 0 && (from != to)) {
						if(dp[nv] > w + arr[from][to]) {
							dp[nv] = w + arr[from][to];
							q.add(new int[] {nv, dp[nv]});
						}
					}
				}
			}
		}
		
		int ans = INF;
		for(int i = 0; i < (1<<(n+1)); i++) {
			if(dp[i] != INF && Integer.bitCount(i) >= p) {
				ans = min(ans, dp[i]);
			}
		}
		if(p == 0) bw.write("0\n");
		else bw.write(((ans == INF)? -1 : ans) + "\n");
		bw.flush();
		bw.close();
	}
}