//BOJ11659 구간 합 구하기 4 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	private static int n, m;
	private static int[] subSum, arr;
	
	public static void main(String[] args) throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		n = nextInt(stk);
		m = nextInt(stk);
		subSum = new int[n];
	
		arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		subSum[0] = arr[0];
		for(int i = 1; i < n; i++) {
			subSum[i] = subSum[i-1] + arr[i];
		}
		
		for(int i = 0; i < m ; i++) {
			stk = new StringTokenizer(br.readLine());
			int s = nextInt(stk) - 1, e = nextInt(stk) - 1;
			bw.write(((s==0)? subSum[e] : (subSum[e] - subSum[s-1])) + "\n");
		}
		
		bw.flush();
		bw.close();
	}
	
	static int nextInt(StringTokenizer stk) {
		return Integer.parseInt(stk.nextToken());
	}
}
