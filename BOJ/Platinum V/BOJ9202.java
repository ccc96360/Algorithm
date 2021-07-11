//BOJ9202 Boggle 20210711
import java.io.*;
import java.util.*;
import java.util.function.Predicate;

public class Main {
    private static final BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    private static int n,m;
    private static Trie trie;
    private static int[] score = {0,0,0,1,1,2,3,5,11};

    private static boolean[][] visited;
    private static int[] dr = {-1, 0, 1, 0, -1, -1, 1, 1};
    private static int[] dc = {0, 1, 0, -1, -1, 1, -1, 1};

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        trie = new Trie();
        for(int i = 0; i < n; i++){
            trie.insert(br.readLine().trim());
        }
        br.readLine();

        m = Integer.parseInt(br.readLine());
        for(int i = 0; i < m; i++){
            String[][] board = new String[4][4];
            for(int j = 0; j < 4; j++){
                board[j] = br.readLine().split("");
            }
            solve(board);
            if(i == m-1) break;
            br.readLine();
        }
        bw.flush();
        bw.close();
    }

    private static void solve(String[][] board) throws IOException {
        Set<String> resultSet = new HashSet<>();
        visited = new boolean[4][4];
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                visited[i][j] = true;
                String curS = board[i][j];
                dfs(new int[]{i, j}, curS, visited, board, resultSet);
                visited[i][j] = false;
            }
        }
        int point = 0, mx = -1;
        String ans = "";
        for(String s: resultSet){
            int length = s.length();
            point += score[length];
            if(length > mx){
                mx = length;
                ans = s;
            }else if(length == mx){
                if(ans.compareTo(s) > 0){
                    ans = s;
                }
            }
        }
        bw.write(point + " " + ans + " " + resultSet.size() + "\n");
    }


    public static void dfs(int[] v, String curS, boolean[][] visited, String[][] board, Set<String> result){
        int r = v[0], c = v[1];
        if(trie.contains(curS)){
            result.add(curS);
        }
        if(curS.length() == 8) return;
        for(int i = 0; i < 8; i++){
            int nr = r + dr[i], nc = c + dc[i];

            if(isInRange(nr, nc) && !visited[nr][nc]){
                String ns = curS + board[nr][nc];
                if(trie.isPrefix(ns)) {
                    visited[nr][nc] = true;
                    dfs(new int[]{nr, nc}, ns, visited, board, result);
                    visited[nr][nc] = false;
                }
            }
        }
    }

    public static boolean isInRange(int r, int c){
        Predicate<Integer> v = (x) -> (0 <= x && x < 4);
        return v.test(r) && v.test(c);
    }
    static class Node{
        private String data = "";
        private Map<String, Node> children = new HashMap<>();
        private boolean isLast = false;

        public Node(String data) {
            this.data = data;
        }

        public boolean isLast() {
            return isLast;
        }

        public void setLast(boolean last) {
            isLast = last;
        }

        public Map<String, Node> getChildren() {
            return children;
        }
    }

    static class Trie{
        private Node root = new Node("");

        public void insert(String word){
            Node curNode = this.root;
            for(String s: word.split("")){
                if (!curNode.getChildren().containsKey(s)) {
                    curNode.getChildren().put(s, new Node(s));
                }
                curNode = curNode.children.get(s);
            }
            curNode.setLast(true);
        }

        public boolean isPrefix(String word){
            Node curNode = this.root;
            for(String s: word.split("")){
                if(!curNode.children.containsKey(s)) return false;
                curNode = curNode.children.get(s);
            }
            return true;
        }

        public boolean contains(String word){
            Node curNode = this.root;
            for(String s: word.split("")){
                if(!curNode.children.containsKey(s)) return false;
                curNode = curNode.children.get(s);
            }
            return curNode.isLast();
        }
    }
}