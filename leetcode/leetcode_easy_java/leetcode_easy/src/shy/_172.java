package shy;

public class _172 {
	public int trailingZeroes(int n) {
		return n == 0 ? 0 : trailingZeroes(n / 5) + n / 5;
	}
}
