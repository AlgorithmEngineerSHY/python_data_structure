package shy;

public class _191 {
	public int hammingWeight(int n) {
		int ones = 0;
		while (n != 0) {
			ones += n & 1;
			n >>>= 1;
		}
		return ones;
	}
}