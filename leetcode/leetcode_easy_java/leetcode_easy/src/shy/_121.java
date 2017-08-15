package shy;

import java.util.ArrayList;

public class _121 {
	public int maxProfit(int[] prices) {
		if (prices.length == 0 || prices.length == 1)
			return 0;
		ArrayList<Integer> arrayList = new ArrayList<Integer>();
		for (int i = 0; i < prices.length - 1; i++) {
			arrayList.add(prices[i + 1] - prices[i]);
		}
		int sum_max = 0;
		int sum_tmp = 0;
		for (int i = 0; i < arrayList.size(); i++) {
			sum_tmp = Math.max(sum_tmp + arrayList.get(i), arrayList.get(i));
			sum_max = Math.max(sum_max, sum_tmp);
		}
		return sum_max;
	}
}
