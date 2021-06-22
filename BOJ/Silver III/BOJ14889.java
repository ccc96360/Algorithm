//BOJ14889 스타트와 링크 20210622
import java.io.*;
import java.util.*;

import static java.lang.Math.abs;
import static java.lang.Math.min;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static int n;
    private static int[][] info;


    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        info = new int[n][n];
        for(int i = 0; i < n; i ++){
            int j = 0;
            for(String s: br.readLine().split(" ")){
                info[i][j] = Integer.parseInt(s);
                j++;
            }
        }
        Boolean[] members = new Boolean[n];
        Arrays.fill(members, false);

        int ans = selectTeam(0, members, 0);
        bw.write(ans + "\n");
        bw.flush();
        bw.close();
    }
    public static int getTeamPower(Boolean[] members){
        int a = 0, b = 0;
        for(int i = 0; i < n; i++) {
            Boolean team = members[i];
            for(int j = 0; j < n; j++){
                int w = info[i][j];
                if(members[j] == team){
                    if(team)
                        a += w;
                    else
                        b += w;
                }
            }
        }
        return abs(a-b);
    }
    public static int selectTeam(int v, Boolean[] members, int size){
        if(size == n / 2){
            return getTeamPower(members);
        }
        else{
            int ret = Integer.MAX_VALUE;
            for(int i = v; i < n; i++){
                if(!members[i]){
                    members[i] = true;
                    ret = min(selectTeam(i+1, members, size+1), ret);
                    members[i] = false;
                }
            }
            return ret;
        }
    }
}