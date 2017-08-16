package shy;

import java.util.HashSet;
import java.util.Set;

public class _217 {
	public boolean containsDuplicate(int[] nums) {
		Set<Integer> set = new HashSet<Integer>();
		for (int i : nums) {
			if (!set.add(i))
				return true;
		}
		return false;
	}
}
