//BOJ7578 공장 20210716
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	static int PIV = 1 << 20;
	static int n;
	static int[] A, B, location, tree;
	static List<int[]> edges = new ArrayList<>();

	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		A = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		B = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
		location = new int[1000001];
		tree = new int[PIV*2];
		
		for(int i = 0; i < n; i++) {
			location[B[i]] = i;
		}
		for(int i = 0; i < n; i++) {
			edges.add(new int[] {i, location[A[i]]});
		}
		
		Comparator<int[]> comp = (a,b) -> (a[0] == b[0])? Integer.compare(a[1], b[1]) : Integer.compare(a[0], b[0]);
		Collections.sort(edges, comp);
		long ans = 0;
		for(int[] edge: edges) {
			int v = edge[1];
			if(v != n-1) {
				ans += query(v+1, n-1);
			}
			update(v);
		}
		bw.write(ans + "\n");
		bw.flush();
		bw.close();
	}
	
	static int query(int l, int r) {
		int ret = 0;
		l += PIV; r += PIV;
		while(l <= r) {
			if(l % 2 == 1) ret += tree[l++];
			if(r % 2 == 0) ret += tree[r--];
			l /= 2;
			r /= 2;
		}
		return ret;
	}
	
	static void update(int n) {
		n += PIV;
		tree[n] += 1;
		while((n/2) > 0) {
			n /= 2;
			tree[n]++;
		}
		
	}
}

