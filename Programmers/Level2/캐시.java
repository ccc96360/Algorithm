//캐시 2018 카카오 BLIND RECRUITMENT 20211005
import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        if(cacheSize == 0) return cities.length * 5;
        int answer = 0;
        Map<String, Integer> cache = new TreeMap<>();
        int nice = 0;
        
        for(String v : cities){
            String city = v.toLowerCase();
            if(cache.containsKey(city)){
                answer += 1;
            }else{
                answer += 5;
                if(cache.size() >= cacheSize){
                    cache.remove(findLRUKey(cache));
                }
            }
            cache.put(city, nice++);
        }
    
        return answer;
    }
    
    private String findLRUKey(Map<String, Integer> cache){
        String ret = "";
        int min = Integer.MAX_VALUE;
        for(String key : cache.keySet()){
            if(min > cache.get(key)){
                ret = key;
                min = cache.get(key);
            }
        }
        return ret;
    }
}