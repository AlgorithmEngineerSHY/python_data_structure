package shy;

public class _204 {
	public int countPrimes(int n) {
		boolean[] cuishuo = new boolean[n];
		int r = 0;
		for (int i = 2; i < n; i++) {
			if (cuishuo[i] == false) {
				r++;
				for (int j = 2; j * i < n; j++)
					cuishuo[j * i] = true;
			}
		}
		return r;
	}
}
