//BOJ11866 요세푸스 문제 0 20210614
import java.io.*;
import java.util.*;
import java.util.List;

public class BOJ11866 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        StringTokenizer in = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(in.nextToken());
        int k = Integer.parseInt(in.nextToken());

        ArrayDeque<Integer> q = new ArrayDeque<>();
        for(int i = 1; i <= n; i++){
            q.addLast(i);
        }

        List<Integer> ans = new ArrayList<Integer>();
        int cnt = 1;
        while(!q.isEmpty()){
            if(cnt < k){
                q.addLast(q.pollFirst());
                cnt++;
            }
            else{
                ans.add(q.pollFirst());
                cnt = 1;
            }
        }
        System.out.print("<");
        for(int i = 0; i < n-1; i++){
            int v = ans.get(i);
            System.out.print(v + ", ");
        }
        System.out.println(ans.get(n-1)+">");
    }
}
