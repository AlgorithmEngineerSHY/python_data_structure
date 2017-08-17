package shy;

import java.util.LinkedList;
import java.util.Queue;

public class MyStack {
	private Queue<Integer> queue = new LinkedList<Integer>();

	public void push(int x) {
		queue.add(x);
		for (int i = 1; i < queue.size(); i++)
			queue.add(queue.poll());
	}

	public int pop() {
		return queue.poll();
	}

	public int top() {
		return queue.peek();
	}

	public boolean empty() {
		return queue.isEmpty();
	}
}
