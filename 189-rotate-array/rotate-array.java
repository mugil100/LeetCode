class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length; 
        k = k % n;
        swap(nums, 0, n-1);
        swap(nums, 0, k-1);
        swap(nums, k, n-1);
    }

    private void swap(int[] nums, int start, int stop){
        while (start<stop){
            int temp = nums[start];
            nums[start] = nums[stop];
            nums[stop] = temp;
            start++;
            stop--;
        }
    }
}