//BOJ14003 가장 긴 증가하는 부분 수열 5 20210715
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static int PIV = 1 << 20;
	static int n;
	static int[] tree = new int[PIV * 2], arr, trace;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		Map<Integer, Integer> compressSet = new HashMap<Integer, Integer>();
		int idx = 1;
		int[] sortedArr = arr.clone();
		Arrays.sort(sortedArr);
		for(int v: sortedArr) {
			if(!compressSet.containsKey(v)) {
				compressSet.put(v, idx++);
			}
		}
		
		trace = new int[n];
		int ans = 0;
		for(int i = 0; i < n; i++) {
			int v = compressSet.get(arr[i]);
			
			int frontNum = query(0, v-1);
			trace[i] = frontNum + 1;
			if(tree[PIV + v] != trace[i]) update(v, trace[i]);
			ans = max(ans, trace[i]);
		}
		
		
		int tmp = ans;
		int[] ansSet = new int[ans];
		for(int i = n-1; i >= 0; i--) {
			if(trace[i] == tmp) {
				ansSet[--tmp] = arr[i];
			}
		}
		bw.write(ans + "\n");
		for(int i = 0; i < ans - 1; i++) {
			bw.write(ansSet[i] + " ");
		}
		bw.write(ansSet[ans-1] + "\n");
		bw.flush();
		bw.close();
		
	}
	
	static void update(int n, int v) {
		n += PIV;
		tree[n] = v;
		while((n/2) > 0) {
			n /= 2;
			tree[n] = max(tree[n*2], tree[n*2 + 1]);
		}
	}
	
	static int query(int l, int r) {
		int ret = 0;
		l += PIV;
		r += PIV;
		while(l <= r) {
			if(l % 2 == 1) ret = max(ret, tree[l++]);
			if(r % 2 == 0) ret = max(ret, tree[r--]);
			l /= 2;
			r /= 2;
		}
		return ret;
	}
	
	static int nextInt(StringTokenizer stk){
		return Integer.parseInt(stk.nextToken());
	}
}
