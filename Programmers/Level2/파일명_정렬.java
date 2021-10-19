//파일명 정렬 2018 카카오 BLIND RECRUITMENT 20211019
import java.util.*;
import java.util.stream.*;

class Solution {
    public String[] solution(String[] filesRaw) {
        int n = filesRaw.length;
        String[] answer = new String[n];
        List<File> files = Arrays.stream(filesRaw)
            .map(File::new)
            .collect(Collectors.toList());
        Collections.sort(files);
        
        for(int i = 0; i < n; i++){
            answer[i] = files.get(i).toString();
        }
        return answer;
    }
    
    
    class File implements Comparable{
        String head;
        String number;
        String tail;
        
        File(){}
        File(String fileName){
            boolean findDigit = false;
            int digitStartIdx = 0, digitEndIdx = fileName.length();
            char[] arr = fileName.toCharArray();
            for(int i = 0; i < fileName.length(); i++){
                char c = arr[i];
                if(Character.isDigit(c)){
                    if(!findDigit){
                        findDigit = true;
                        digitStartIdx = i;
                    } 
                }else{
                    if(findDigit){
                        digitEndIdx = i;
                        break;
                    }
                }
            }
            head = fileName.substring(0, digitStartIdx);
            number = fileName.substring(digitStartIdx, digitEndIdx);
            tail = fileName.substring(digitEndIdx);
        }
        
        String getHead(){ return head; }
        String getNumber(){ return number; }
        String getTail(){ return tail; }
        
        @Override
        public int compareTo(Object o){
            File other = (File) o;
            String mHead = head.toLowerCase();
            String oHead = other.getHead().toLowerCase(), oNumber = other.getNumber();
            if(oHead.equals(mHead)){
                return Integer.parseInt(number) -  Integer.parseInt(oNumber);
            }else{
                return mHead.compareTo(oHead);
            }
        }
        
        @Override
        public String toString(){
            return head + number + tail;
        }
    }
}