//BOJ1991 트리 순회 20210707
import java.io.*;
import java.util.*;

import static java.lang.Math.*;

public class Main {
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    private static int n;
    private static Map<String, String[]> adj;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        adj = new HashMap<>();

        for(int i = 0; i < n; i++){
            String[] tmp = br.readLine().split(" ");
            adj.put(tmp[0], new String[]{tmp[1], tmp[2]});
        }


        preorder("A");
        bw.write("\n");
        inorder("A");
        bw.write("\n");
        postorder("A");

        bw.flush();
        bw.close();
    }

    public static void preorder(String v) throws IOException {
        bw.write(v);
        String left = adj.get(v)[0];
        String right = adj.get(v)[1];
        if(!left.equals(".")) preorder(left);
        if(!right.equals(".")) preorder(right);
    }
    public static void inorder(String v) throws IOException {
        String left = adj.get(v)[0];
        String right = adj.get(v)[1];
        if(!left.equals(".")) inorder(left);
        bw.write(v);
        if(!right.equals(".")) inorder(right);
    }
    public static void postorder(String v) throws IOException {
        String left = adj.get(v)[0];
        String right = adj.get(v)[1];
        if(!left.equals(".")) postorder(left);
        if(!right.equals(".")) postorder(right);
        bw.write(v);
    }
}