//BOJ2164 카드2 20210614
import java.io.*;
import java.util.ArrayDeque;

public class BOJ2164 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for(int i = 1; i <= n; i++){
            q.addLast(i);
        }
        int size = q.size();
        while(size > 1){
            q.pollFirst();
            size--;
            if(size == 1) break;
            q.addLast(q.pollFirst());
        }
        System.out.println(q.getFirst());
    }
}
