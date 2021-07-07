//BOJ11003 최솟값 찾기 20210707
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer stk = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(stk.nextToken());
        int l = Integer.parseInt(stk.nextToken());

        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        Deque<Integer> dq = new ArrayDeque<>();
        for(int i = 0; i < n; i++){
            int v = arr[i];
            while (!dq.isEmpty() && arr[dq.getLast()] > v)
                dq.removeLast();
            dq.addLast(i);
            if(dq.getFirst() < i - l + 1)
                dq.removeFirst();
            bw.write(arr[dq.getFirst()] + " ");
        }
        bw.flush();
        bw.close();
    }
}