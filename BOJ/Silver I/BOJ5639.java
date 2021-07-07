//BOJ5639 이진 검색 트리 20210707
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n;
    private static int[] preorder;

    public static void main(String[] args) throws IOException {

        List<Integer> arr = new ArrayList<>();
        while (true){
            String in = br.readLine();
            if(in == null) break;
            arr.add(Integer.parseInt(in));
        }

        n = arr.size();
        preorder = arr.stream().mapToInt(Integer::intValue).toArray();

        search(0, n-1);
        bw.flush();
        bw.close();

    }

    public static void search(int s, int e) throws IOException {
        int root = preorder[s];
        if(s == e){
            bw.write(preorder[s] + "\n");
            return;
        }
        else if(s > e){
            return;
        }
        int ne = s + 1;
        for(int i = s + 1; i <= e; i++){
            if(preorder[i] > root) {
                ne = i;
                break;
            }
        }

        search(s + 1, ne - 1);
        search(ne, e);
        bw.write(root + "\n");
    }
}