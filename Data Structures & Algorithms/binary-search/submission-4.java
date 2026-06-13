class Solution {
    public int search(int[] nums, int target) {
        int l = 0; 
        int r = nums.length - 1;
        int midPoint = (l + r) / 2;
        while (l <= r) {
            midPoint = (l + r) / 2;
            if (nums[midPoint] == target) {
                return midPoint;
            }

            else if (target < nums[midPoint]) {
                r = midPoint - 1;
            }

            else {
                l = midPoint + 1;
            }
        }
        return -1;
    }
}
