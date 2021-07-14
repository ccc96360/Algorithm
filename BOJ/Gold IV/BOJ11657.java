//BOJ11657 타임머신 20210714
import java.io.*;
import java.util.*;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	private static int INF = Integer.MAX_VALUE;
	private static int n, m;
	private static int[][] edges;
	private static long[] ans;
	
	public static void main(String[] args) throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		n = nextInt(stk);
		m = nextInt(stk);
		
		ans = new long[n+1];
		edges = new int[m][3];
		
		for(int i = 0; i < m; i++) {
			stk = new StringTokenizer(br.readLine());
			int u = nextInt(stk), v = nextInt(stk), w = nextInt(stk);
			edges[i] = new int[]{u, v, w};
		}
		if(!bellmanFord(1)) {
			bw.write(-1 + "\n");
		}else {
			for(int i = 2; i <= n; i++) {
				bw.write(((ans[i] == INF)? -1 : ans[i]) + "\n");
			}
		}
		bw.flush();
		bw.close();
	}
	
	public static boolean bellmanFord(int start) {
		Arrays.fill(ans, INF);
		ans[start] = 0;
		for(int i = 1; i <= n; i ++) {
			for(int[] e: edges) {
				int cur = e[0], next = e[1], w = e[2];
				
				if(ans[cur] == INF) continue;
				if(ans[next] > ans[cur] + w) {
					ans[next] = ans[cur] + w;
					if(i == n) return false;
				}
			}
		}
		return true;
	}
	
	public static int nextInt(StringTokenizer stk) {
		return Integer.parseInt(stk.nextToken());
	}
}
