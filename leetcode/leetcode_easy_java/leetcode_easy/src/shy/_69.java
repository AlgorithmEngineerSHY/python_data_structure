package shy;

public class _69 {
	public int mySqrt(int x) {
		double result = x / 2.0;
		while (Math.abs(result * result - x) >= 0.5) {
			result -= (result * result - x) / (2.0 * result);
		}
		return (int) result;
	}

}
