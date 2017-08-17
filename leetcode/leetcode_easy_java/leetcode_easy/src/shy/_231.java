package shy;

public class _231 {
	public boolean isPowerOfTwo(int n) {
		if (n <= 0)
			return false;
		int r = 0;
		for (int i = 1; i <= 31; i++) {
			if ((n & 1) == 1) {
				r++;
			}
			if (r > 1)
				return false;
			n >>>= 1;
		}
		return true;
	}
}
