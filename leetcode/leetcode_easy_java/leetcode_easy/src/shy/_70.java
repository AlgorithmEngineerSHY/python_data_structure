package shy;

public class _70 {
	public int climbStairs(int n) {
		int num_max_2 = n / 2;
		int num_1;
		double result = 0;
		for (int i = num_max_2; i >= 0; i--) {
			num_1 = n - 2 * i;
			result += factorial(i, num_1);
		}
		return (int)result;
	}

	public double factorial(int a, int b) {
		double r = 1.0;
		for (int i = a + 1; i <= a + b; i++) {
			r *= i;
		}
		for (int i = 1; i <= b; i++) {
			r /= i;
		}
		return r;
	}
}
