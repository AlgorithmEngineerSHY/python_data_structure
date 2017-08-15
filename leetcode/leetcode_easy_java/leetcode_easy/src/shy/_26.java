package shy;

public class _26 {
	public int removeDuplicates(int[] nums) {
		if (nums.length <= 1)
			return nums.length;
		int n = 0;
		for (int i : nums) {
			if (nums[n] < i) {
				nums[++n] = i;
			}
		}
		return n + 1;
	}
}
