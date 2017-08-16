package shy;

import java.util.HashSet;
import java.util.Set;

public class _202 {
	public boolean isHappy(int n) {
		Set<Integer> set = new HashSet<Integer>();
		int r, tmp;
		while (set.add(n)) {
			r = 0;
			while (n > 0) {
				tmp = n % 10;
				r += Math.pow(tmp, 2);
				n /= 10;
			}
			if (r == 1)
				return true;
			else
				n = r;
		}
		return false;

	}
}
