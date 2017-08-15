package shy;

import java.util.ArrayList;
import java.util.List;

public class _119 {
	public List<Integer> getRow(int rowInt) {
		List<Integer> list = new ArrayList<Integer>();
		if (rowInt < 0)
			return list;
		for (int i = 0; i < rowInt + 1; i++) {
			list.add(0, 1);
			for (int j = 1; j < list.size() - 1; j++)
				list.set(j, list.get(j) + list.get(j + 1));
		}
		return list;
	}
}
