class Solution {
    public int maxFrequencyElements(int[] nums) {
        //using hashmap
        Map<Integer, Integer> hm=new HashMap<>();
        int freq=0, count=0;
        for(int i: nums){
            hm.put(i,hm.getOrDefault(i,0)+1);
        }
        for(int i:hm.values()){
            if(i==freq){
                count+=1;
            }
            else if(i>freq){
                freq=i;
                count=1;
            }
        }
        return count*freq;
    }
}