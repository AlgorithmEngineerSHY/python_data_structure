package shy;

public class _27 {
	public int removeElement(int[] nums, int val) {
		if (nums.length == 0)
			return 0;
		int a = 0;
		for (int i : nums) {
			if (i != val) {
				nums[a++] = i;
			}
		}
		return a;

	}

}
