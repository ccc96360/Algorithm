//BOJ3860 할로윈 묘지 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	private static int RIP = -1, WARP = -2, INF = Integer.MAX_VALUE;
	private static int n, w, h, g, e;
	private static int[][] board;
	private static List<int[]> edges;
	private static long[] ans;
	
	private static int[] dr = {-1, 0, 1, 0};
	private static int[] dc = {0, 1, 0, -1};
	
	public static void main(String[] args) throws IOException {
		while(solve());		
		bw.flush();
		bw.close();
	}
	
	public static boolean solve() throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		w = nextInt(stk); h = nextInt(stk);
		if(w == 0 && h == 0) return false;
		n = w * h;
		
		board = new int[h][w];
		edges = new ArrayList<int[]>();
		
		g = Integer.parseInt(br.readLine());
		for(int i = 0; i < g; i++) {
			stk = new StringTokenizer(br.readLine());
			int c = nextInt(stk), r = nextInt(stk);
			board[r][c] = RIP;
		}

		e = Integer.parseInt(br.readLine());
		for(int i = 0; i < e; i++) {
			stk = new StringTokenizer(br.readLine());
			int c1 = nextInt(stk), r1 = nextInt(stk), c2 = nextInt(stk), r2 = nextInt(stk), weight = nextInt(stk);
			board[r1][c1] = WARP;
			edges.add(new int[] {pointToInt(r1, c1), pointToInt(r2,c2), weight});
		}
		
		for(int r = 0; r < h; r++) {
			for(int c = 0; c < w; c++) {
				if(r == h - 1 && c == w - 1) continue;
				if(board[r][c]!=0) continue;
				for(int i = 0; i < 4; i++) {
					int nr = r + dr[i], nc = c + dc[i];
					if((0 <= nr && nr < h) && (0 <= nc && nc < w)) {
						if(board[nr][nc] != RIP) {
							edges.add(new int[] {pointToInt(r, c), pointToInt(nr, nc), 1});
						}
					}
				}
			}
		}
		
		ans = new long[n];
		if(!bellmanFord(0)) {
			bw.write("Never\n");
		}else {
			bw.write(((ans[n-1] == INF)?  "Impossible" : ans[n-1]) + "\n");
		}
		return true;
	}
	
	public static boolean bellmanFord(int start) {
		Arrays.fill(ans, INF);
		ans[start] = 0;
		for(int i = 0; i < n; i++) {
			for(int[] edge: edges) {
				int cur = edge[0], next = edge[1], weight = edge[2];
				
				if(ans[cur] == INF) continue;
				if(ans[next] > ans[cur] + weight) {
					ans[next] = ans[cur] + weight;
					if(i == n - 1) return false;
				}
				
			}
		}
		return true;
	}
	public static int pointToInt(int r, int c) {
		return r * w + c;
	}
	
	public static int nextInt(StringTokenizer stk) {
		return Integer.parseInt(stk.nextToken());
	}
}
