package shy;

import java.util.HashMap;

public class _1 {
	public int[] twoSum(int[] nums, int target) {
		HashMap<Integer, Integer> hash_map = new HashMap<Integer, Integer>();
		for (int i = 0; i < nums.length; i++) {
			if (hash_map.containsKey(nums[i])) {
				return new int[] { hash_map.get(nums[i]), i };

			} else {
				hash_map.put(target - nums[i], i);
			}
		}
		return new int[] { 0, 0 };
	}

}
