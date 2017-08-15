package shy;

public class _7 {
	public int reverse(int x) {
		int result = 0;
		while (x != 0) {
			int tail = x % 10;
			int tmp_result = result * 10 + tail;
			if ((tmp_result - tail) / 10 != result) {
				return 0;
			}
			result = tmp_result;
			x = x / 10;
		}
		return result;
	}
}
