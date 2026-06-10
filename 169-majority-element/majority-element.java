class Solution {
    public int majorityElement(int[] nums) {
        int cand = nums[0];
        int count = 1;

        for(int i=1; i < nums.length; i++){
            if(nums[i] != cand){
                if(count == 0){
                    cand = nums[i];
                }
                else{
                    count--;
                }
            }
            else{
                count++;
            }
        }

        return cand;
        
    }
}