package shy;

import java.util.ArrayList;

public class MinStack {

	/** initialize your data structure here. */
	ArrayList<Integer> arrayList = new ArrayList<Integer>();
	int min;

	public MinStack() {

	}

	public void push(int x) {
		if (arrayList.isEmpty()) {
			min = x;
			arrayList.add(x);
		} else {
			min = Math.min(min, x);
			arrayList.add(x);

		}

	}

	public void pop() {
		int tmp = arrayList.get(arrayList.size() - 1);
		arrayList.remove(arrayList.size() - 1);
		if (tmp == min) {

			if (!arrayList.isEmpty()) {
				min = arrayList.get(0);
				for (int i : arrayList) {
					min = Math.min(i, min);
				}
			}

		}

	}

	public int top() {
		return arrayList.get(arrayList.size() - 1);

	}

	public int getMin() {
		return min;

	}
}
