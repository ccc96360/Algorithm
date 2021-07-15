//BOJ11660 구간 합 구하기 5 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	private static int n, m;
	private static int[][] subSum, arr;
	
	public static void main(String[] args) throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		n = nextInt(stk);
		m = nextInt(stk);
		subSum = new int[n][n];
		
		arr = new int[n][n];
		for(int i = 0; i < n; i++) {
			arr[i] = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		}
		
		for(int i = 0; i < n; i++) {
			subSum[i][0] = arr[i][0];
		}
		for(int i = 0; i < n; i++) {
			for(int j = 1; j < n; j++) {
				subSum[i][j] = subSum[i][j-1] + arr[i][j];
			}
		}
		
		while(m-- > 0){
			stk = new StringTokenizer(br.readLine());
			int r1 = nextInt(stk) - 1, c1 = nextInt(stk) - 1, r2 = nextInt(stk) - 1, c2 = nextInt(stk) - 1;
			int ans = 0;
			for(int i = r1; i <= r2; i++) {
				ans += ((c1 == 0)? subSum[i][c2] : (subSum[i][c2] - subSum[i][c1-1]));
			}
			bw.write(ans + "\n");
		}
		
		bw.flush();
		bw.close();
	}
	
	static int nextInt(StringTokenizer stk) {
		return Integer.parseInt(stk.nextToken());
	}
}
