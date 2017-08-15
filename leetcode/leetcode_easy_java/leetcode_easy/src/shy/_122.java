package shy;

import java.util.ArrayList;

public class _122 {
	public int maxProfit(int[] prices) {
		if (prices.length <= 1)
			return 0;
		ArrayList<Integer> arrayList = new ArrayList<Integer>();
		for (int i = 0; i <= prices.length - 2; i++) {
			arrayList.add(prices[i + 1] - prices[i]);
		}
		int result = 0;
		for (int i : arrayList) {
			if (i > 0) {
				result += i;
			}
		}
		return result;
	}
}
