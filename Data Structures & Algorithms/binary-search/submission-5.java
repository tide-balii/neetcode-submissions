class Solution {
    public int recBinarySearch (int l, int r, int m, int[] nums, int target) {
        if (l > r) return - 1; 

        else if (nums[m] == target) return m; 

        else if (target < nums[m]) {
            r = m - 1;
            return recBinarySearch (l, r, ((l + r) / 2), nums, target); 
        }

        else {
            l = m + 1;
            return recBinarySearch (l, r, (l + r) / 2, nums, target); 
        }

    }
    
    public int search(int[] nums, int target) {
        return recBinarySearch(0, nums.length - 1, (nums.length - 1) / 2, nums, target);
    }
}
