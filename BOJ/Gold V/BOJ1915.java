//BOJ1915 가장 큰 정사각형 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int n, m;
	static int[][] arr;
	static int[] dr = {-1, 0, -1}; 
	static int[] dc = {0, -1, -1};
	
	public static void main(String[] args) throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		n = nextInt(stk); m = nextInt(stk);
		
		arr = new int[n][m];
		for(int i = 0; i < n; i++) {
			arr[i] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
		}
		
		int ans = 0;
		for(int r = 0; r < n; r++) {
			for(int c = 0; c < m; c++) {
				if(arr[r][c] == 0) continue;
				int mn = 1001;
				for(int i = 0; i < 3; i++) {
					int nr = r + dr[i], nc = c + dc[i];
					if(0 <= nr && nr < n && 0 <= nc && nc < m) {
						mn = min(arr[nr][nc], mn);
					}else {
						mn = 0;
					}
				}
				arr[r][c] = mn + 1;
				ans = max(ans, arr[r][c]);
			}
		}
		
		
		bw.write((ans*ans) + "\n");
		bw.flush();
		bw.close();
	}
	
	static int nextInt(StringTokenizer stk){
		return Integer.parseInt(stk.nextToken());
	}
}
