package shy;

import java.util.ArrayList;
import java.util.List;

public class _118 {
	public List<List<Integer>> generate(int numRows) {
		List<List<Integer>> list = new ArrayList<List<Integer>>();
		if (numRows == 0)
			return list;
		if (numRows == 1) {
			List<Integer> list_tmp = new ArrayList<Integer>();
			list_tmp.add(1);
			list.add(list_tmp);
			return list;
		}
		if (numRows == 2) {
			list.add(new ArrayList<Integer>() {
				{
					add(1);
				}
			});
			list.add(new ArrayList<Integer>() {
				{
					add(1);
					add(1);
				}
			});
			return list;
		}
		list.add(new ArrayList<Integer>() {
			{
				add(1);
			}
		});
		list.add(new ArrayList<Integer>() {
			{
				add(1);
				add(1);
			}
		});
		for (int i = 1; i <= numRows - 2; i++) {
			List<Integer> list_tmp_ = new ArrayList<Integer>();
			List<Integer> list_last = list.get(list.size() - 1);
			list_tmp_.add(1);
			int len = list_last.size() - 1;
			for (int j = 0; j <= len - 1; j++) {
				list_tmp_.add(list_last.get(j) + list_last.get(j + 1));
			}
			list_tmp_.add(1);
			list.add(list_tmp_);

		}
		return list;
	}
}
