package shy;

public class _53 {
	public int maxSubArray(int[] nums) {
		int sum_max = nums[0];
		int sum = nums[0];
		for (int i = 1; i < nums.length; i++) {
			sum = Math.max(sum + nums[i], nums[i]);
			sum_max = Math.max(sum_max, sum);
		}
		return sum_max;

	}
}
