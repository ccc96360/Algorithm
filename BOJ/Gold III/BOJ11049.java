//BOJ11049 행렬 곱셈 순서 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int n, m;
	static List<int[]> matrices = new ArrayList<>();
	static int[][] d;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < n; i++) {
			StringTokenizer stk = new StringTokenizer(br.readLine());
			matrices.add(new int[] {nextInt(stk), nextInt(stk)});
		}
		d = new int[n][n];
		bw.write(dp(0, n-1) + "\n");
		bw.flush();
		bw.close();
	}
	
	static int dp(int s, int e) {
		int ret = Integer.MAX_VALUE;
		if(s == e) return 0;
		if(d[s][e] != 0) return d[s][e];
		for(int i = s; i < e; i++) {
			int a = matrices.get(s)[0] , b = matrices.get(i+1)[0], c = matrices.get(e)[1]; 
			ret = min(ret, dp(s, i) + dp(i + 1, e) + a * b * c);
		}
		d[s][e] = ret;
		return ret;
	}
	
	static int nextInt(StringTokenizer stk){
		return Integer.parseInt(stk.nextToken());
	}
}
