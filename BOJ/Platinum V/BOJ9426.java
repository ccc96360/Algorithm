//BOJ9426 중앙값 측정 20210714
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	private static int PIV = 1 << 16;
	private static int n, k;
	private static int[] tree = new int[PIV * 2];
	
	public static void main(String[] args) throws IOException {
		StringTokenizer stk = new StringTokenizer(br.readLine());
		n = nextInt(stk);
		k = nextInt(stk);
		
		Queue<Integer> q = new LinkedList<Integer>();
		long ans = 0;
		for(int i = 0; i < n; i++) {
			int v = Integer.parseInt(br.readLine());
			if(q.size() < k-1) {
				q.add(v);
				update(v,1);
			}else {
				q.add(v);
				update(v, 1);
				ans += findMedian();
				int front = q.poll();
				update(front, -1);
			}
		}
		bw.write(ans + "\n");
		
		
		bw.flush();
		bw.close();
	}
	static int findMedian() {
		int ret = 0, idx = 1, findIdx = (k-1) / 2;
		while((idx*2) < PIV * 2) {
			if(findIdx < tree[idx*2]) {
				idx = idx * 2;
			}else {
				findIdx -= tree[idx*2];
				idx = idx * 2 + 1;
			}
		}
		ret = idx-PIV;
		return ret;
	}
	
	static void update(int idx, int v) {
		idx += PIV;
		tree[idx] += v;
		while((idx/2) > 0) {
			idx /= 2;
			tree[idx] = tree[idx * 2] + tree[idx * 2 + 1];
		}
	}
	
	static int nextInt(StringTokenizer stk) {
		return Integer.parseInt(stk.nextToken());
	}
}
