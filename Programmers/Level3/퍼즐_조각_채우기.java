//퍼즐 조작 채우기 위클리 챌린지 3주차 20211016
import java.util.*;

import static java.lang.Math.*;
class Solution {
    
    final int BLOCK = 1, EMPTY = 0;
    
    int n, emptyNum, blockNum;
    int[] dr = {-1, 0, 1, 0};
    int[] dc = {0, 1, 0, -1};
    
    List<Block> blocks, emptySpaces;
    
    public int solution(int[][] game_board, int[][] table) {
        n = game_board.length;
        
        blocks = getBlocks(BLOCK, table);
        emptySpaces = getBlocks(EMPTY, game_board);
        emptyNum = emptySpaces.size();
        blockNum = blocks.size();
        
        int answer = 0;
        boolean[] selectedBlock = new boolean[blockNum];
        for(int i = 0; i < emptyNum; i++){
            Block space = emptySpaces.get(i);
            
            boolean filled = false;
            for(int j = 0; j < blockNum; j++){
                
                if(selectedBlock[j]) continue;
                
                Block block = blocks.get(j);
                if(space.getSize() != block.getSize()) continue;
                
                for(int k = 0; k < 4; k++){
                    if(space.isFit(block)){
                        selectedBlock[j] = true;
                        filled = true;
                        answer += block.getSize();
                        break;
                    }
                    block.rotate();
                }
                
                if(filled) break;
            }
        }
        return answer;
    }
    
    public List<Block> getBlocks(int type, int[][] table){
        List<Block> blocks = new ArrayList<>();
        boolean[][] visited = new boolean[n][n];
        for(int r = 0; r < n; r++){
            for(int c = 0; c < n; c++){
                if(visited[r][c]) continue;
                if(table[r][c] != type) continue;
                Block block = getBlock(type, visited, table, r, c);
                blocks.add(block);
            }    
        }
        return blocks;
    }
    
    public Block getBlock(int type, boolean[][] visited, int[][] table, int sr, int sc){
        List<int[]> points = new ArrayList<>();
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{sr, sc});
        visited[sr][sc] = true;
        
        int mr = n, mc = n;
        while(!q.isEmpty()){
            int[] tmp = q.poll();
            int r = tmp[0], c = tmp[1];
            mr = min(r, mr);
            mc = min(c, mc);
            points.add(tmp);
            
            for(int i = 0; i < 4; i++){
                int nr = r + dr[i], nc = c + dc[i];
                if((0 <= nr && nr < n) && (0 <= nc && nc < n)){
                    if(table[nr][nc] != type) continue;
                    if(visited[nr][nc]) continue;
                    visited[nr][nc] = true;
                    q.add(new int[]{nr, nc});
                }
            }
        }
        
        
        return new Block(points, mr, mc);
    }
    
    class Block{
        List<int[]> info;
        int size = 0;
        
        Block(){}
        Block(List<int[]> points, int sr, int sc){
            size = points.size();
            info = new ArrayList<>();
            for(int[] point : points){
                int r = point[0], c = point[1];
                info.add(new int[]{r - sr, c - sc});
            }
            info.sort((a, b) -> {
                if(a[0] == b[0]){
                    return a[1] - b[1];
                }
                return a[0] - b[0];
            });
        }
        
        boolean isFit(Block other){
            if(other.getSize() != size) return false;
            List<int[]> oInfo = other.getInfo();
            for(int i = 0; i < size; i ++){
                int[] p1 = info.get(i), p2 = oInfo.get(i);
                if(!(p1[0] == p2[0] && p1[1] == p2[1])) return false;
            }
            return true;
        }
        
        void rotate(){
            List<int[]> points = new ArrayList<>();
            int mr = 50, mc = 50;
            for(int[] p : info){
                mr = min(mr, p[1]);
                mc = min(mc, 5 - p[0]);
                points.add(new int[]{p[1], 5 - p[0]});
            }
            info.clear();
            for(int[] p : points){
                info.add(new int[]{p[0] - mr, p[1] - mc});
            }
            info.sort((a, b) -> {
                if(a[0] == b[0]){
                    return a[1] - b[1];
                }
                return a[0] - b[0];
            });
        }
        int getSize(){
            return size;
        }
        List<int[]> getInfo(){
            return info;
        }
        
    }
}