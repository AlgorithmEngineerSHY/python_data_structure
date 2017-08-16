package shy;

public class _198 {
	public int rob(int[] nums) {
		int last = 0, curr = 0;
		for (int i = 0; i < nums.length; i++) {
			int tmp = Math.max(curr, last + nums[i]);
			last = curr;
			curr = tmp;
		}
		return curr;
	}
}
